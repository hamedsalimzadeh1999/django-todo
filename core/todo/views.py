from django.shortcuts import render,redirect
from .models import task
# Create your views here.
def index(request):
    MyTodoList = task.objects.all()
    context ={'mytask':MyTodoList}
    return render(request, 'index.html' , context)

def AddTask(request):
    mytask = request.POST['task']
    task(TaskTitle=mytask).save()
    return redirect(request.META['HTTP_REFERER'])



def DeletTask(request,taskid):
    task.objects.filter(id=taskid).delete()
    return redirect(request.META['HTTP_REFERER'])