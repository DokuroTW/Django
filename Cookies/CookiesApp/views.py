from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def new_cookie(request,key=None,value=None):
    response = HttpResponse('Cookie 存起來了')
    response.set_cookie(key,value)
    return response 

def get_cookie(request,key=None):
    if key in request.COOKIES:
        return HttpResponse('%s:%s' %(key,request.COOKIES[key]))
    else:
        return HttpResponse('cookie 不存在!!')
    
def get_allcookie(request):
    if request.COOKIES != None:
        str=''
        for key1,value1 in request.COOKIES.items():
            str= str + key1 + ':' + value1 + '<br>'
        return HttpResponse('%s' %(str))
    else:
        return HttpResponse("cookie 不存在")

def DeleteCookie(request,key=None):
    if key in request.COOKIES:
        response = HttpResponse('刪除Cookie:'+key)
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('沒有Cookie:'+key)
    
def SetTimeCookie(request,key=None,value=None):
    response= HttpResponse('只有3600秒喔')
    response.set_cookie(key,value,max_age=3600)
    return response

def index(request):
    if 'counter' in request.COOKIES:
        counter=int(request.COOKIES['counter'])
        counter+=1
    else:
        counter=1
    response=HttpResponse('目前瀏覽次數'+str(counter))
    tomorrow= datetime.datetime.now()+datetime.timedelta(days=1)
    tomorrow= datetime.datetime.replace(tomorrow,hour=0,minute=0,second=0)
    time=datetime.datetime.strftime(tomorrow,'%a,%d-%b-%Y %H:-%M:-%S GMT')
    response.set_cookie('counter',counter,expires=time)

    return response
     
