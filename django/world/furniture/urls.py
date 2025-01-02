from django.contrib import admin
from django.urls import path, include
from furniture import views
urlpatterns = [
    path('admin', views.admin, name=('admin')),
    path('', views.good, name=('good'))
    
]
