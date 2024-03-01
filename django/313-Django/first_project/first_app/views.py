from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Department, Employee

# Create your views here.

def index(request):
    emp_list = Employee.objects.all()
    emp_dict = {'emp' : emp_list}
    return render(request, 'first_app/index.html', context = emp_dict)

# def index(request):
#     # return HttpResponse('Hello World')
#     dict = {
#         "insert_me" : "This is from views.py", 
#         "fname" : "John",
#         "lname" : "Smith",
#         "age" : "3000"
#     }
#     return render(request, 'first_app/index.html', context=dict)

def about(request):
    dict = {
        "insert_me" : "This is from views.py", 
        "fname" : "Rose",
        "lname" : "Tyler",
        "age" : "sad"
    }
    return render(request, 'first_app/about.html', context=dict) 