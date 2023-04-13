from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
def adduser (request):
    try:
        user=User.objects.get(username='test')
    except:
        user=None
    if user != None:
        return HttpResponse(user.username + '帳號已建立')
    else:
        user = User.objects.create_user("test","test@test.com.tw","a123456")
        user.first_name='Wen'
        user.last_name='Lin'
        user.is_staff=True
        user.save()
        return redirect('/admin/')
    
def index(request):
    if request.user.is_authenticated:
        name=request.user.username
    return render (request,'index.html',locals())

def login(request):
    if request.method =='POST':
        LoginName = request.POST['username']
        LoginPW =request.POST['password']
        LoginUser = authenticate(username=LoginName,password=LoginPW)
        if LoginUser is not None:
            if LoginUser.is_active:
                auth.login(request,LoginUser)
                message='登入成功'
                return redirect("/index/")
            else:
                message='你已經停權'
        else:
            message='您輸入錯誤,登入失敗'
    return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')