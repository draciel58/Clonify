from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import RegisterForm,SigninForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Products


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
				'We urge to serve you the best way possible! Founders - Aziz Sharif, Mukul Choudhury',
				'dracielraven589@gmail.com',
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


def laptop(request):
	drazil = Products.objects.filter(product='laptop')
	return render(request,'cloneapp/laptop.html',{'laptop':drazil})

def mobile(request):
	drazil = Products.objects.filter(product='mobile')
	return render(request,'cloneapp/mobile.html',{'mobile':drazil})

def speaker(request):
	drazil = Products.objects.filter(product='speakers')
	return render(request,'cloneapp/speaker.html',{'speaker':drazil})
