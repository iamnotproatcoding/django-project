from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, "rubik-shop/home.html")

def about_page(request):
    return HttpResponse("<h1>Blog About</h1>")