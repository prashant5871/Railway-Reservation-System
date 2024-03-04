from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')


def login_user(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')