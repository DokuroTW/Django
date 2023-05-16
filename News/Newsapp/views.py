from django.shortcuts import render
from Newsapp import models
import math
# Create your views here.
page1=1

def index(request ,pageindex=None):
    global page1
    pagesize=8
    newsall= models.NewsTable.objects.all().order_by('-id')
    datasize= len(newsall)
    totpage= math.ceil(datasize/pagesize)

    if pageindex == None:
        page1=1
        newstable=models.NewsTable.objects.filter(enable=True).order_by('-id')[:pagesize]

    elif pageindex == 'prev':
        start = (page1-2)*pagesize
        if start >=0:
            newstable=models.NewsTable.objects.filter(enable=True).order_by('-id')[start:(start+pagesize)]
            page1 -= 1
    elif pageindex =='next':
        start = page1*pagesize
        if start < datasize:
            newstable=models.NewsTable.objects.filter(enable=True).order_by('-id')[start:(start+pagesize)]
            page1 +=1

    elif pageindex =='home':
        start = (page1-1)*pagesize
        newstable=models.NewsTable.objects.filter(enable=True).order_by('-id')[start:(start+pagesize)]    
    
    currentpage =page1
    return render(request,'index.html',locals())

def detail(request,detailid=None):
    table = models.NewsTable.objects.get(id=detailid)
    catego=table.catego
    title=table.title
    pubtime=table.pubtime
    fakename=table.fakename
    message=table.message
    table.press +=1
    table.save()
    return render(request,'detail.html',locals())