from django.urls import path , include
from .views import index,addtask
urlpatterns = [
    path('' , index),
    path("add", addtask, name="add"),
]