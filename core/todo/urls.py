from django.urls import path , include
from .views import index,DeletTask
urlpatterns = [
    path('' , index),
    path("edit/<int:taskid>/", DeletTask, name="DeletTask"),
]