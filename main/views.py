from django.shortcuts import render, redirect
from .models import TypeArticle, Articles, Comments
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.


def home(request):
    article = Articles.objects.all().order_by('-types__level')
    type_article = TypeArticle.objects.all()
    return render(request, "main/home.html", {"article": article, "type_article": type_article})


def article(request, i):
    article = Articles.objects.filter(types_id = i)
    return render(request, "main/article.html", {"article": article})


def detail(request, id):
    search_article = Articles.objects.filter(id = id)
    search_commentary = Comments.objects.filter(comment_id = id)
    print(search_commentary)
    return render(request, "main/detail.html", {"article":search_article, "comment": search_commentary})
    
  
def comment(request, id):
    if request.user.is_authenticated:
        if request.method  == "POST":
            search_article = Articles.objects.filter(id = id)
            com = Comments()
            com.title_id = request.user.id
            com.comment_id = id
            com.text = request.POST.get("commentary")
            com.save()
        
            return redirect(f"/article/detail/{id}")
        elif request.method == "GET":
            return redirect(f"/article/detail/{id}")
    else:
        return redirect("/users/login?next=/")
    

def post_get(request):
    type_article = TypeArticle.objects.all()
    return render(request, "main/post.html", {"type_article":type_article })


def post_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            article = Articles()
            article.title = request.POST.get("title")
            article.link_for_image = request.POST.get("image")
            article.text = request.POST.get("text")
            article.owner_id = request.user.id
            article.types_id = request.POST.get("type_id")
            article.save()
            return redirect("mypost")
        elif request.method == "GET":
            return redirect("/articles/post")
    else:
        return redirect("/users/login?next=/")


def mypost(request):
    if request.user.is_authenticated:
        article = Articles.objects.filter(owner_id = request.user.id)
        return render(request, "main/my_post.html", {"article":article})
    else:
        return redirect("/users/login?next=/")
    

def delete(request, id):
    search_article = Articles.objects.filter(id = id)
    search_article.delete()
    return redirect("mypost")


def edit_get(request, id):
    search_article = Articles.objects.filter(id = id)
    return render(request, "main/edit.html", {"search_article":search_article})

def edit_post(request, id):
    search_article = Articles.objects.get(id = id)
    search_article.title = request.POST.get("title")
    search_article.image = request.POST.get("image")
    search_article.text = request.POST.get("text")
    search_article.save()
    return redirect("mypost")

def go(request):
    return redirect("/")