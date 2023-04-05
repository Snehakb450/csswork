from django.shortcuts import render

# Create your views here.
def get_master(request):
    return render(request,"css/master.html")

def get_home(request):
    return render(request,"css/home.html")

def get_courses(request):
    return render(request,"css/courses.html")

def get_contact(request):
    return render(request,"css/contact.html")

