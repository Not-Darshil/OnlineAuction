from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm

#authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def homepage(request):
    # return HttpResponse("request")
    return render(request,'myapp/homepage.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("my_login")
    
    
    context={'registerform':form}
    return render(request,'myapp/register.html',context=context)

def my_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect ("dashboard")
    context={'loginform':form}

    return render(request,'myapp/my_login.html',context=context)


def user_logout(request):
    auth.logout(request)    
    return redirect("")


@login_required(login_url="my_login") # for protecting the view of dashboard

def dashboard(request):
    return render(request,'myapp/dashboard.html')


