from django.shortcuts import render ,redirect
from CRUDapp.models import student
from CRUDapp.form import PostForm
# Create your views here.

def index(request):                                #使用Django 內建函式呼叫 DB資料
    students = student.objects.all().order_by('id')
    return render(request,"index.html",locals())

def post1(request):                               #使用 method POST 方式 傳遞 Table 儲存到DB
	
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

def post2(request):                              #使用 Form函式 驗證資料 與 method POST 方式  儲存到DB
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

def delete(request,id=None):                 #透過method POST 以ID為媒介 刪除所選取的 表格資料
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

def edit(request,id=None,mode=None):				#透過 GET 抓取資料庫資料 並更新資料(比較危險一般不會這樣寫)
	if mode == "edit":                              # edit.html 的button按下去後 才會做動(action="/edit/{{unit.id}}/edit")
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
			unit=student.objects.get(id=id)         #這邊主要功能是把unit.cBirtday的年月日改為"-"
			strdate=str(unit.cBirthday)
			strdate2=strdate.replace('年','-')
			strdate2=strdate.replace('月','-')
			strdate2=strdate.replace('日','-')
			unit.cBirthday=strdate2
		except:
			message='id不存在'
		return render(request,"edit.html",locals())


def edit2(request,id=None,mode=None):			#透過 POST 抓取資料庫資料 並更新資料(比較安全)		
	if mode =="save":							# edit.html 的button按下去後 才會做動(action="/edit2/{{unit.id}}/save")
		unit=student.objects.get(id=id)
		unit.cName=request.POST['edit2_name']
		unit.cSex=request.POST['edit2_sex']
		unit.cBirthday=request.POST['edit2_birthday']
		unit.cEmail=request.POST['edit2_email']
		unit.cPhone=request.POST['edit2_phone']
		unit.cAddr=request.POST['edit2_addr']
		unit.save()
		message="已存檔"
		return redirect('/')
	elif mode =="load":
												 #這邊主要功能是把unit.cBirtday的年月日改為"-"
		unit=student.objects.get(id=id)		
		strdate=str(unit.cBirthday)
		strdate2=strdate.replace('年','-')
		strdate2=strdate.replace('月','-')
		strdate2=strdate.replace('日','-')
		unit.cBirthday=strdate2
		return render(request,'edit2.html',locals())
		



		#Django內建的 CRUD功能分別是 C:create()  R: all()\get()  U: save()  D: delete()
		  