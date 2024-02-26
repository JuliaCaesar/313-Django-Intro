from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    dict = {
        "insert_me" : "This is from views.py", 
        "fname" : "John",
        "lname" : "Smith",
        "age" : "3000"
    }
    return render(request, 'first_app/index.html', context=dict)

def about(request):
    return HttpResponse('<h1>This is the About Page</h1>') 