from django.urls import path , include
from .views import index,DeleteTask,AddTask,EditTask,Edittaskaction
urlpatterns = [
    path('' , index,name='index'),
    path("add/",AddTask , name="AddTask"),
    path("DeleteTask/<int:taskid>/", DeleteTask, name="DeletTask"),
    path("edit/<int:taskid>/",EditTask,name="edittask"),
    path("edit/<int:taskid>/action/",Edittaskaction,name="edittask")

]