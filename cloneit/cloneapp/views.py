from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import RegisterForm,SigninForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def home(request):
	return render(request, 'cloneapp/home.html')

def signupuser(request):
	if request.method=='GET':
		return render(request, 'cloneapp/signupuser.html',{'form':RegisterForm()})
	else:	
		if request.POST['password']==request.POST['confirm_password']:
			user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
			user.save()
			email_message = request.POST['email']
			send_mail(
				'Welcome To Clonify!',
				'We urge to serve you the best way possible!',
				'Founders - Aziz Sharif, Mukul Choudhury',
				'azizsharif2000@gmail.com',
				'stuffmukuldoes@gmail.com',
				[email_message],
				fail_silently=False
				)
			login(request,user)
			return redirect('home')
		else:
			return render(request, 'cloneapp/signupuser.html',{'form':RegisterForm(),'error':'passwords didnt matched'})


@login_required
def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('signupuser')


def loginuser(request):
	if request.method=='GET':
		return render(request, 'cloneapp/loginuser.html',{'form':SigninForm()})
	else:
		user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request, 'cloneapp/loginuser.html',{'form':SigninForm(),'error':'username and password is incorrect'})
		else:
			login(request,user)
			return redirect('home')

