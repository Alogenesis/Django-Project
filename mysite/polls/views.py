from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("<h1>Hello, world. Home Page</h1>")

def home_page_html(request):
    tags = ['น้ำตก','ธรรมชาติ','ทะเล','ป่าดงดิบ']
    rating = 3
    return render(request,'index.html',
    {'name':'Object ข้อมูล ที่โยนเข้าหน้าเว็บ',
     'auther':'Winai Nob',
     'tags':tags,
     'rating':rating,
     })

def page1(request):
    return render(request, 'page1.html',)