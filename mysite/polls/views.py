from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User


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

def createRegister(request):
    return render(request, 'register.html', )

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword : #เช็คว่า password 2 ช่องตรงกันมั้ย ถ้าตรงไปต่อ
        if User.objects.filter(username=username).exists(): #เช็คว่า username ซ้ำกับที่เคยลงไว้มั้ย
            print("Username นี้มีคนใช้แล้ว")
            return redirect('/register')
        elif User.objects.filter(email=email).exists(): #เช็คว่า email ซ้ำมั้ย
            print("Email นี้มีผู้ใช้งานแล้ว")
            return redirect('/register')
        else:   #ถ้าไม่ซ้ำ ให้ทำการบันทึกข้อมูล
            User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname,
            )
            User.save()
            return redirect('/')
    else:   #password ไม่ตรงกัน ลงทะเบียนใหม่
        return redirect('/register')
