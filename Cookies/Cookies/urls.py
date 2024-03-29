"""Cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from CookiesApp import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('admin/', admin.site.urls),
    path('new_cookie/<str:key>/<str:value>/',views.new_cookie),
    path('get_cookie/<str:key>/',views.get_cookie),
    path('get_allcookie/',views.get_allcookie),
    path('SetTimeCookie/<str:key>/<str:value>/',views.SetTimeCookie),
    path('DeleteCookie/<str:key>',views.DeleteCookie),
]
