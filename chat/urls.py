"""chat urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='index'),
    path('groups/', views.group_list, name="groups"),
    path('create/', views.create_group, name='create'),
    path('chat/transform/<str:room_name>/', views.room, name='room'),
    path('', views.post_help, name = "post"),
    path('chat/<int:id>/', views.post_post, name = "post"),
    path('id/<str:room_id>/', views.group_view, name='room'),
    path('messages/user/<str:username>/', views.find_user, name = "username")
    
]
