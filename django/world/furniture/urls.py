from django.contrib import admin
from django.urls import path, include
from furniture import views
urlpatterns = [
    path('', views.home, name=('home')),
    path('home/', views.home, name=('home')),
    path('stock/', views.stock, name='stock'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name=('contact')),
    path('work/', views.work, name=('work')),
    # path('furniture/', include('furniture.urls'))
]