from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
#each object below is a model which is indicated by models.Model in their constructors
#CharField and IntegerField define datatypes and qualifications on the models
#The variables that the Fields are equal to are the names for that specifc field
#ForeignKey indicates that each choice is realted to a single question
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text
		

'''
TO MAKE MODEL CHANGES:
change models in models.py
run python manage.py makemigrations
run python manage.py migrate
'''