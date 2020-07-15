from django.db import models

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
	price = models.DecimalField(max_digits=7,decimal_places=2)

	def __str__(self):
		return self.name
