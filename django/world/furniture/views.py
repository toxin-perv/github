from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stock(request):
    # return HttpResponse("")
    context = {'name' : 'ranjan', 'lan' : 'django'}
    return render(request, 'stock.html', context)
def blog(request):
    return HttpResponse("Blog Page")

def admin(request):
    return HttpResponse("admin page")

def good(rwquest):
    return HttpResponse("this work is good")