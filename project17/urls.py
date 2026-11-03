"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app17 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/',views.insertaccount,name='newaccount'),
    path('sucess',views.success,name='account_view'),
    path('',views.home,name='home'),
    path('balance/',views.balance,name='balance'),
    path('deposit/',views.deposit,name='deposit'),
    path('tranfer/',views.transferaccount,name='transfer'),
    path('withdraw/',views.withdrawaccount,name='withdraw'),
    path('close/', views.closeaccount, name='closeaccount'),
    path('about/', views.about, name='about'),
    ]

