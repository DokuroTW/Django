from django import forms

class PostForm(forms.Form):
	name = forms.CharField(max_length=20,initial='')
	sex = forms.CharField(max_length=2,initial='M')	
	birthday = forms.DateField()
	email = forms.EmailField(max_length=100,initial='',required=False)
	phone = forms.CharField(max_length=50,initial='',required=False)
	addr = forms.CharField(max_length=255,initial='',required=False)