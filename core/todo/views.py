from django.shortcuts import render
from .models import task
# Create your views here.
def index(request):
    MyTodoList = task.objects.all()
    context ={'mytask':MyTodoList}
    return render(request, 'index.html' , context)

def addtask(request):
    pass