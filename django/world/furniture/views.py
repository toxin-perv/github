from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stock(request):
    return HttpResponse("Stock Page")

def blog(request):
    return HttpResponse("Blog Page")

def admin(request):
    return HttpResponse("admin Page")