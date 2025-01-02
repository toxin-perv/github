from django.contrib import admin
from django.urls import path, include
from furniture import views
urlpatterns = [
    path('', views.work, name=('work'))
    
]
