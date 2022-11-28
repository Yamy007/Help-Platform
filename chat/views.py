import secrets
import json
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Chat, Customize,Room ,PostHelp, TypePostHelp


def post_help(request: object):
    choose = TypePostHelp.objects.all()
    new_post = PostHelp.objects.all().order_by("-date")
    return render(request, "chat/post.html", {"choose":choose, "post": new_post})

def post_post(request: object, id):
    find = PostHelp.objects.filter(id = id)
    check_user_1 = Room.objects.filter(user_1 = find[0].owner)
    check_user_2 = Room.objects.filter(user_2 = request.user.username)
    if len(check_user_1) == 0  and len(check_user_2) == 0:
        
    
        create_hash = secrets.token_hex(nbytes=16)
        
        
        room = Room()
        room.user_1  = find[0].owner
        room.name = create_hash
        room.reason = find[0].title
        room.user_2 = request.user.username
        room.save()
        return redirect(f"/chat/chat/transform/{create_hash}")
    else:

        search_user_1 = Room.objects.filter(user_1= find[0].owner)
        search_room = search_user_1.filter(user_2 = request.user.username)
        return redirect(f"/chat/chat/transform/{search_room[0].name}")


    
    
def user(request: object):
    user = request.user

    if user.is_authenticated:
        your_groups = Chat.your_group(user)
        your_room_owner = Room.objects.filter(user_1 = request.user )
        your_room = Room.objects.filter(user_2 = request.user.username)
        return render(request, "chat/user.html", {"rooms": your_room_owner, "room": your_room})
    else:
        redirect("/users/login")
        

def room(request: object, room_name: str):
    room_name = slugify(room_name, allow_unicode=True)
    if room_name == "listener":
        return redirect("/chat/listener2")
    user = request.user
    chat_model = Chat.objects.filter(name=room_name)
    if chat_model.exists():
        chat_model[0].members.add(user)
    else:
        chat = Chat.objects.create(name=room_name)
        chat.members.add(user)
    chat = Chat.objects.get(name=room_name)
    room_id = chat.room_id
    return redirect(f'/chat/id/{room_id}')


def group_list(request: object):
    color_fields = Customize.get_all_fields()
    all_groups = Chat.all_groups()
    paginator = Paginator(all_groups, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    context = {**context, **color_fields}
    return render(request, "chat/group-list.html", context)


def create_group(request: object):
    return render(request, "chat/create-group.html")


@login_required(login_url="auth:register")
def group_view(request: object, room_id: str):
    color_fields = Customize.get_all_fields()
    listener_room = Chat.objects.filter(name="listener")
    if not listener_room.exists():
        Chat.objects.create(name="listener")
    listener: Chat = Chat.objects.get(name="listener")
    if room_id == listener.room_id:
        return redirect("/chat/listener2")
    user = request.user
    chat_model = Chat.objects.filter(room_id=room_id)
    if chat_model.exists():
        chat_model[0].members.add(user)
    else:
        return redirect("index")
    username = request.user.username
    context = {
        "room_id": room_id,
        "username": mark_safe(json.dumps(username)),
        "name": user,
        "room": chat_model[0].name,
        "listener_id": listener.room_id
    }
    context = {**context, **color_fields}
    return render(request, "chat/room.html", context)

