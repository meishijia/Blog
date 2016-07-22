from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import traceback


def index(request):
    return render(request,'accounts/login.html')

def login_do(request):
    username = request.POST['username']
    password = request.POST['password']
    request.session["username"] = username
    user = authenticate(username = username,password = password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/articles/index')
        else:
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

@login_required
def logout_do(request):
    logout(request)
    return HttpResponseRedirect('/accounts/index')

def register(request):
    return render(request,'accounts/register.html')

def deal_register(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username,email,password)
        user.save()
    except:
        print traceback.print_exc()
    return render(request,'accounts/login.html')



# Create your views here.

