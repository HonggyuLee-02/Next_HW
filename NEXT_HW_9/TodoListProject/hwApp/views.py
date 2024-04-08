from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime
import pytz

# 'Asia/Seoul' 시간대 객체 생성
seoul_tz = pytz.timezone('Asia/Seoul')

# Create your views here.
def home(request):
    #Logic here
    Todolist = Todo.objects.all().order_by("deadline")
    if request.method == 'POST':
        status, pk = request.POST['is_completed'].split('-')[0], request.POST['is_completed'].split('-')[1]
        if status == 'True':
            Todo.objects.filter(pk = pk).update(
                is_completed=True
            )
        else:
            Todo.objects.filter(pk = pk).update(
                is_completed=False
            )
        return redirect('home')
    for todo in Todolist:
        delta = todo.deadline.date() - datetime.now(tz=seoul_tz).date()
        todo.dday = delta
    
        if delta.days == 0:
            todo.dday = "D-day!"
        else:
            todo.dday = f"D-{delta.days}"
            
        if todo.is_completed == False:
            todo.status = '미완료'
        else:
            todo.status = '완료'
        
    return render(request,'home.html',{'Todolist':Todolist,})

def detail(request, detail_pk):
    #Logic here
    todo = Todo.objects.get(pk = detail_pk)
    if todo.is_completed == False:
            todo.status = '미완료'
    else:
            todo.status = '완료'
    return render (request,'detail.html',{'todo':todo,})

def update(request, update_pk):
    #Logic here
    todo = Todo.objects.get(pk = update_pk)
    
    if request.method == 'POST':
        updated_todo = Todo.objects.filter(pk=update_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail',detail_pk=update_pk)
    return render(request,'update.html',{'todo':todo,})

def new(request):
    #Logic here
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
            is_completed = False,
        )
        return redirect('home')
    return render(request,'new.html')

def delete(request, delete_pk):
    #Logic here
    delobj = Todo.objects.get(pk=delete_pk)
    delobj.delete()
    return redirect('home')