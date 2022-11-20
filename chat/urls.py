"""chat urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.group_list, name="groups"),
    path('create/', views.create_group, name='create'),
    path('<str:room_name>/', views.room, name='room'),
    path('id/<str:room_id>/', views.group_view, name='room'),
]
