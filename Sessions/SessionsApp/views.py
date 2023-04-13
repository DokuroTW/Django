from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def NewSession(request,key=None,value=None):
    response = HttpResponse("Session已儲存")
    request.session[key]=value
    return response

def GetSession(request,key=None):
    if key in request.session:
        return HttpResponse('%s : %s' %(key,request.session[key]))
    else:
        return HttpResponse('Session 不存在')

def GetAllSessions(request):
    if request.session !=None:
        strsessions=''
        for key,value in request.session.items():
            strsessions = strsessions +key+":"+str(value) +'<br>'
            return HttpResponse(strsessions)
    else:
        return HttpResponse("Session不存在")
    
def vote (request):
    if not 'vote' in request.session:
        request.session['vote']=True
        return HttpResponse('您是第一次投票')
    else:
        return HttpResponse('你已經投票過了喔!!!')
    
def TimeSession (request,key=None,value=None):
    response = HttpResponse("已經儲存Session持續時間30s")
    request.session['key']=value
    request.session.set_expiry(30)
    return response

def DeleteSession(request,key=None):
    if key in request.session:
        del request.session['key']
        return HttpResponse("已刪除"+key)
    else:
        return HttpResponse("Session不存在")


def login(request):
    TrueUsername='99123'
    TruePassword='12399'
    status= 'logout'
    if request.method == 'POST':
        if not 'username' in request.session :
            if request.POST['username']==TrueUsername and request.POST['password']==TruePassword:
                status = 'login'
                request.session['username']=TrueUsername
                message='登入成功'
            else:
                message='登入錯誤'

    else:
        if 'username' in request.session :
            if request.session['username']==TrueUsername:     
                status = 'login'
                message='你已經登入過了'
    return render(request,'login.html',locals())     
            
def logout(request):
    if 'username' in request.session:
        del request.session['username']
        message ='登出成功'
        status= 'logout'
    return render(request,'login.html',locals())





