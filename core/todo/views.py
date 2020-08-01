from django.shortcuts import render,redirect
from .models import task
# Create your views here.
def index(request):
    MyTodoList = task.objects.all()
    context ={'mytask':MyTodoList}
    return render(request, 'index.html' , context)


def AddTask(request):
    mytask = request.POST['task']
    task(TaskTitle = mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def DeleteTask(request,taskid):
    task.objects.filter(id=taskid).delete()
    return redirect(request.META['HTTP_REFERER'])

def EditTask(request , taskid):
    context = {'taskid':taskid}
    return render(request , "edit.html",context)

def Edittaskaction (request , taskid):
    edittask = request.POST['task']
    todo = task.objects.filter(id = taskid)[0]
    todo.TaskTitle = edittask
    todo.save()
    return redirect('index')