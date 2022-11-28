from django.urls import path
from .views import *

urlpatterns = [

    path("test/<int:id>/", index),
    path("test/<int:id>/result", result),
    path("about", about),
    path("", choose)
]
