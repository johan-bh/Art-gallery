from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class AboutText(models.Model):
	title = models.CharField(max_length=100,null=True)
	text_1 = models.CharField(max_length=1000, null=True)
	text_2 = models.CharField(max_length=1000, null=True)
	text_3 = models.CharField(max_length=1000, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
		return self.text_1
		return self.text_2
		return self.text_3

class ContactText(models.Model):
	text = models.CharField(max_length=500, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.text

class UploadImage(models.Model):
	image = models.ImageField(upload_to='gallery_image',null=True)



