from django.shortcuts import render

# Create your views here.
def count(request):
    #logics here
    return render(request, 'count.html')

# Create your views here.
def result(request):
    #logics here
    text = request.POST['text']
    length_of_words =len(text.strip().split())
    length_of_text = len(text.strip())
    length_without_space = len(text.strip().replace(' ', ''))
    return render(request, 'result.html',{'length_of_words': length_of_words,
                                          'length_of_text':length_of_text,
                                          'length_without_space':length_without_space})