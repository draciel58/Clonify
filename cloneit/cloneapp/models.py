from django.db import models
from django.contrib.auth.models import User

product_choices=(
	('laptop','laptop'),
	('mobile','mobile'),
	('headphone','headphone'),
	('speakers','speakers'),
	('keyboard', 'keyboard'),
	)
	

class Products(models.Model):
	product = models.CharField(max_length=20,choices= product_choices,default='laptop')
	name = models.CharField(max_length=50,blank=True)
	short_description = models.TextField(max_length=100,blank=True)
	description = models.TextField(max_length=2000)
	image = models.ImageField(upload_to='cloneapp/image',blank=True)
	price = models.DecimalField(max_digits=18,decimal_places=2)

	def __str__(self):
		return self.name

class Cartitem(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)		
	item = models.CharField(max_length=50,blank=True,null=True)
	quantity = models.IntegerField(default=1)
	price = models.DecimalField(max_digits=18,decimal_places=2,null=True)
	total = models.DecimalField(max_digits=18,decimal_places=2,null=True)

	def __str__(self):
		return f"{self.user} (item)-{self.item} (quantity)-{self.quantity}"	

class Userprofile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)	
	username = models.CharField(max_length=100,blank=True)
	phone_number = models.BigIntegerField(blank=True,null=True)
	email = models.EmailField(max_length=100,blank=True,null=True)
	address = models.TextField(max_length=400,blank=True,null=True)
	profile_picture = models.ImageField(upload_to='cloneapp/profile_image',default='cloneapp/image/asus-zenbook.jpg',blank=True,null=True)
    
	def __str__(self):
		return self.username

	@property	
	def get_photo_url(self):	
		if self.profile_picture and hasattr(self.profile_picture,'url'):
			return self.profile_picture.url
		else:
			return "media/cloneapp/image/s10.jpg"	
