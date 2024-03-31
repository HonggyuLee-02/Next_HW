from django.shortcuts import render

# Create your views here.
def home(request):
    #logics here
    return render(request,'home.html')

def portfolio(request):
    #logics here
    return render(request, 'portfolio.html')