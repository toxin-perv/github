from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def stock(request):
    # return HttpResponse("")
    # context = {'name' : 'ranjan', 'lan' : 'django'}
    return render(request, 'stock.html',)


def blog(request):
    return render(request, 'blog.html')



def work(request):
    return render(request, 'work.html')

def contact(request):
    return render(request, 'contact.html')