from django.urls import path , include
from .views import index,DeleteTask,AddTask
urlpatterns = [
    path('' , index),
    path("add/",AddTask , name="AddTask"),
    path("DeleteTask/<int:taskid>/", DeleteTask, name="DeletTask"),
]