from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("patient")
        else:
            return render(request,"authentication/login.html",
                          {"error":"Invalid username and/or password."})

    return render(request,"authentication/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")