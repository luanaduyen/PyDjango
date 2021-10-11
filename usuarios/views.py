from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def cadastro(resquest):
    return render(resquest, 'cadastro.html') 

def login(request):
    return render(request, 'login.html')