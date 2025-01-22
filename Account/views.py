from django.shortcuts import render

def register(request):
    return render(request,"Accounts/register.html")

def login(request):
    return render(request,"Accounts/login.html")
