from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.http import HttpResponse 
from django.contrib import messages
from .models import Enroller
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.core.mail import send_mail  


# Create your views here.


def home(request):
    

    return render(request,'home.html')



def achievements(request):



    return render(request,'achievements.html')

        
        


def admission(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['number']
            age = request.POST['age']
            msg = request.POST['message']

            enroll = Enroller()
            enroll.name = name
            enroll.email = email
            enroll.number = number
            enroll.age = age
            enroll.msg = msg
            enroll.save()
            messages.success(request,'Your form is submited wait for the response!')

        return render(request,'admission.html')
    else:
        messages.error(request,'You have to login first!')
        return render(request,'auth.html')

def auth(request):


    return render(request,'auth.html')

def signup(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        usern = User.objects.filter(username=username)

        if usern.exists():
            messages.error(request,'This username is already taken')
            return redirect('auth')
        else:
            user = User.objects.create_user(username,email,password)
            user.save()
            messages.success(request,'Your account has been created!')
            login(request,user)
            return redirect('/')
        
    return render(request,'auth.html')



def signin(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'You are now logged in. Have a good day')
            return redirect('home')
        else:
            messages.error(request,'You have entered the wrong username or password!')

            return redirect('auth')

            


    return render(request,'auth.html')


def logout(request):

    auth_logout(request)

    return redirect('home')
        



    

