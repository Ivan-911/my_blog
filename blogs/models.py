from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
	"""Model creating three lines:"title"-capcher, "text"-artical,
	"date_added"- the date created a post """
	title = models.CharField(max_length=60)
	text = models.TextField(max_length=200)
	date_added = models.DateField(auto_now=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	def __str__(self):
		 """Returning rows form of model"""
		 return self.title
