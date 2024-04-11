from django.shortcuts import render,redirect
from .models import Hobby,Food,Programming,Hobby_Comment,Food_Comment,Programming_Comment, Hobby_cocoment, Programming_cocoment, Food_cocoment

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST['category'] == 'Hobby':
            new_hobby = Hobby.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
            )
        elif request.POST['category'] == 'Food':
            new_food = Food.objects.create(
                title = request.POST['title'],
                content = request.POST['content']
            )
        else:
            new_programming = Programming.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
            )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    hobbies = Hobby.objects.all()
    foods = Food.objects.all()
    programmings = Programming.objects.all()
    hobbies_count = Hobby.objects.count()
    foods_count = Food.objects.count()
    programmings_count = Programming.objects.count()
    return render(request, 'list.html', {'hobbies': hobbies,
                                         'foods':foods,
                                         'programmings':programmings,
                                         'hobbies_count':hobbies_count,
                                         'foods_count':foods_count,
                                         'programmings_count':programmings_count,
                                         'whole_count': hobbies_count + foods_count + programmings_count,})
    
def hobby(request, hobby_id):
    article = Hobby.objects.get(pk = hobby_id)
    if request.method == "POST" :
        if request.POST['writer'] : 
            Hobby_Comment.objects.create(
                hobby = article,
                writer = request.POST['writer'],
                content = request.POST['content'],
            )
          
    return render(request,'hobby.html',{'article': article})

def food(request, food_id):
    article = Food.objects.get(pk = food_id)
    if request.method == "post" : 
        Food_Comment.objects.create(
            food=article,
            writer = request.POST['writer'],
            content = request.POST['content'],
        )
    return render(request, 'food.html',{'article': article})

def programming(request, programming_id):
    article = Programming.objects.get(pk = programming_id)
    if request.method == "post" : 
        Programming_Comment.objects.create(
            food=article,
            writer = request.POST['writer'],
            content = request.POST['content'],
        )
    return render(request, 'food.html',{'article': article})


def hobbies(request):
    
    hobbies = Hobby.objects.all()
    return render(request,'hobbies.html',{'hobbies': hobbies,})

def foods(request):
    
    foods = Food.objects.all()
    return render(request, 'foods.html',{'foods':foods,})

def programmings(request):
    
    programmings = Programming.objects.all()
    return render(request,'programmings.html',{'programmings':programmings,})
