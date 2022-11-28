from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = "home"),
    path("article/<int:i>/", article, name = "article"),
    path("article/detail/<int:id>/", detail, name = "detail"),
    path("article/detail/<int:id>/comment", comment, name = "comment"),
    path("article/post", post_get, name = "post_get"),
    path("article/post/create", post_post, name="post_post"),
    path("article/mypost", mypost, name = "mypost" ),
    path("article/mypost/edit/<int:id>/", edit_get, name = "edit_get"),
    path("article/mypost/delete/<int:id>/", delete, name = "delete"),
    path("article/mypost/edit/<int:id>/edit", edit_post, name = "edit_post"),
    path('accounts/profile/', go)
]
