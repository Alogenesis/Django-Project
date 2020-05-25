from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("<h1>Hello, world. Home Page</h1>")

def home_page_html(request):
    tags = ['น้ำตก','ธรรมชาติ','ทะเล','ป่าดงดิบ']
    rating = 3
    #Query Daya
    data = Post.objects.all()
    return render(request,'index.html',
    {'name':'Object ข้อมูล ที่โยนเข้าหน้าเว็บ',
     'auther':'Winai Nob',
     'tags':tags,
     'rating':rating,
     #Query Data
     'post':data,
     })
#ลองสร้าง def query แต่มันใช้ไม่ได้ เลยเอาข้อมูลในนี้ไปใส่ใน ฟังก์ชั่น index page แล้ว
def queryData(reqeust):
    #Query Data From Model
    data = Post.objects.all()
    return render(reqeust,'index.html',{'post':data})



def page1(request):
    return render(request, 'page1.html',)

def createForm(request):
    return render(request, 'form.html',)

def addBlog(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})


