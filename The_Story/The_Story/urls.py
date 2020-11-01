"""The_Story URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('home/<str:key>/', views.catergorypage),
    path('search/', views.search),
    path('home/', views.home),
    path('addUser/', views.addUser),
    path('loginForm/', views.loginForm),
    path('login/', views.login),
    path('logout/', views.logout),
    path('addstory/', views.addstoryform),
    path('savestory/', views.savestory),
    path('readstory/<int:id>/', views.readpage),
    path('readstory/', views.readpage),
    path('upfile/', views.uploadImgHandler)
]
