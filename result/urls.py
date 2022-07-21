from django.contrib import admin
from django.urls import path,include
from result import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('home.html',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact')
]
