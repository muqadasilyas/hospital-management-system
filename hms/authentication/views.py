from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class UserLogin(LoginView):
    template_name = 'authentication/login.html'
    next_page = '/patient/'

class UserLogout(LogoutView):
    next_page = 'login'