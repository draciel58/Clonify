from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import RegisterForm,SigninForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Products,Cartitem,Userprofile


@login_required
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
			show = Userprofile.objects.create(user=request.user,username=request.POST['username'],email = request.POST['email'])
			show.save()
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


@login_required
def laptop(request):
	drazil = Products.objects.filter(product='laptop')
	return render(request,'cloneapp/laptop.html',{'laptop':drazil})


@login_required
def mobile(request):
	drazil = Products.objects.filter(product='mobile')
	return render(request,'cloneapp/mobile.html',{'mobile':drazil})


@login_required
def speaker(request):
	drazil = Products.objects.filter(product='speakers')
	return render(request,'cloneapp/speaker.html',{'speaker':drazil})


@login_required
def keyboard(request):
	drazil = Products.objects.filter(product='keyboard')
	return render(request,'cloneapp/keyboard.html',{'keyboard':drazil})


@login_required
def detail(request,product_id):
	drazil = Products.objects.get(pk=product_id)
	return render(request,'cloneapp/detail.html',{'product':drazil})


@login_required
def add_to_cart(request):
	if request.method=='GET':
		total_price=0
		all_products=Cartitem.objects.filter(user=request.user)
		for i in all_products:
			total_price+=i.total
		return render(request,'cloneapp/cart.html',{'product':all_products,'total_price':total_price})
	else:
		total_price=0
		raven = Cartitem.objects.filter(user=request.user,item=request.POST['name'])
		if raven.exists():
			b = Cartitem.objects.get(user=request.user,item=request.POST['name'],price=request.POST['price'])
			b.quantity+=1
			b.total=b.price*b.quantity
			b.save()
			a=Cartitem.objects.filter(user=request.user)
			for i in a:
				total_price+=i.total
			return redirect('home')
		else:
			a=Cartitem.objects.create(user=request.user,item=request.POST['name'],quantity=1,price=request.POST['price'])
			a.total=a.price*a.quantity
			a.save()
			return redirect('home')


@login_required
def cart_increment(request):
	if request.method=='POST':
		all_products=Cartitem.objects.get(user=request.user,item=request.POST['add'])
		all_products.quantity+=1
		all_products.total=all_products.price*all_products.quantity
		all_products.save()
		return redirect('cart')


@login_required
def cart_decrement(request):
	if request.method=='POST':
		all_products=Cartitem.objects.get(user=request.user,item=request.POST['delete'])
		all_products.quantity-=1
		all_products.total=all_products.price*all_products.quantity
		all_products.save()
		if all_products.quantity==0:
			all_products.delete()
		return redirect('cart')


@login_required
def cart_delete(request):
	if request.method=='POST':
		all_products=Cartitem.objects.get(user=request.user,item=request.POST['trash'])
		all_products.delete()
		return redirect('cart')	


@login_required
def profileview(request):
	show = Userprofile.objects.get(user=request.user)
	return render(request,'cloneapp/profile.html',{'profile':show})


@login_required
def profiledit(request):
	show = Userprofile.objects.get(user=request.user)
	if request.method=='GET':
		form = ProfileForm(instance=show)	
		return render(request,'cloneapp/profileedit.html',{'profile':show,'form':form})
	else:
		form = ProfileForm(request.POST, request.FILES, instance=show)
		form.save()
		return redirect('profileview')	
