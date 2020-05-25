"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('',views.home_page_html),
    #path('',views.queryData),  ไม่สามารถใส่ path 2 อันในหน้าเดียวได้
    path('page1',views.page1),
    path('createForm',views.createForm),
    path('addForm',views.addBlog),

    #path หน้า register
    path('register',views.createRegister),
    #path หน้า addregister ให้เก็บข้อมูล
    path('addUser',views.addUser),

    #path หน้า login
    path('login',views.login),
    #path login_success
    path('login_success',views.login_success),


]
