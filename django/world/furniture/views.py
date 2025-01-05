from django.shortcuts import render
from django.http import HttpResponse
from furniture.models import contact
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
    if request.method=="post":
        email = request.post['email']
        password = request.post['password']
        print(email, password)
        ins = contact(email=email, password=password)
        ins.save()
        print("The data has been written to the database")


    return render(request, 'contact.html')
    