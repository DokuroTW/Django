from django.shortcuts import render ,redirect
from CRUDapp.models import student
from CRUDapp.form import PostForm
# Create your views here.

def index(request):
    students = student.objects.all().order_by('id')
    return render(request,"index.html",locals())

def post(request):
	if request.method == "POST":		
		mess = request.POST['username'] 
	else:
		mess="表單資料尚未送出!"	
	return render(request, "post.html", locals())

def post1(request):
	
	if request.method == "POST":
		Name= request.POST['name']
		Sex=request.POST['sex']
		Birthday=request.POST['birthday']
		Email=request.POST['email']
		Phone=request.POST['phone']
		Addr=request.POST['addr']

		unit = student.objects.create(cName=Name,cSex=Sex,cBirthday=Birthday,cEmail=Email,
				cPhone=Phone,cAddr=Addr)
		unit.save()
		return redirect('/')
	else:
		message = '請輸入資料(沒有驗證的版本)'

	return render(request,"post1.html",locals())

def post2(request):  #
	if request.method == "POST": 
		postform = PostForm(request.POST) 
		if postform.is_valid():			
			Name = postform.cleaned_data['name'] 
			Sex =  postform.cleaned_data['sex']
			Birthday =  postform.cleaned_data['birthday']
			Email = postform.cleaned_data['email']
			Phone =  postform.cleaned_data['phone']
			Addr =  postform.cleaned_data['addr']
			
			unit = student.objects.create(cName=Name, cSex=Sex, cBirthday=Birthday, cEmail=Email,cPhone=Phone, cAddr=Addr) 
			unit.save()  
			
			return redirect('/')	
		else:
			message = '驗證錯誤！'	
	else:
		message = '請輸入姓名、性別、生日，其他選填'
		postform = PostForm()
	return render(request, "post2.html", locals())	

def delete(request,id=None):
	if id != None:
		if request.method =="POST":
			ID = request.POST['cId']
			try:
				unit= student.objects.get(id=ID)
				unit.delete()
				return redirect('/')
			except:
				message="讀取錯誤"


	return render(request,"delete.html",locals())

def edit(request,id=None,mode=None):
	if mode == "edit":
		unit = student.objects.get(id=id)
		unit.cName=request.GET['edit_name']
		unit.cSex=request.GET['edit_sex']
		unit.cBirthday=request.GET['edit_birthday']
		unit.cEmail=request.GET['edit_email']
		unit.cPhone=request.GET['edit_phone']
		unit.cAddr=request.GET['edit_addr']
		unit.save()
		message="修改完成"
		return redirect('/index/')
	else:
		try:
			unit=student.objects.get(id=id)
		except:
			message='id不存在'
		return render(request,"edit.html",locals())


def edit2(request,id=None,mode=None):
	if mode == "load":

		unit=student.objects.get(id=id)		
		
		return render(request,'edit2.html',locals())
	elif mode =="save":
		unit=student.objects.get(id=id)
		unit.cName=request.GET['edit2_name']
		unit.cSex=request.GET['edit2_sex']
		unit.cBirthday=request.GET['edit2_birthday']
		unit.cEmail=request.GET['edit2_email']
		unit.cPhone=request.GET['edit2_phone']
		unit.cAddr=request.GET['edit2e_addr']
		unit.save()
		message="已存檔"
		return redirect('/')
		