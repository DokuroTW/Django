from django.shortcuts import render
from app.models import student
# Create your views here.
def listone(request):
    
    try:
        unit = student.objects.get(cName='李采茜')
    except:
        errormessage="(讀取錯誤!!!)"
    return render(request,"listone.html",locals())



def index(request):
    students = student.objects.all().order_by('-id')
    return render(request,"index.html",locals())