from django.db import models
from django.db.models.aggregates import Max
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)
  

    def __str__(self):
       return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.IntegerField()
    option_one=models.CharField(max_length=100) 
    option_two=models.CharField(max_length=100)
    option_three=models.CharField(max_length=100,blank=True)
    option_four=models.CharField(max_length=100,blank=True)
    marks=models.IntegerField(default=1)

    def __str__(self):
        return f'{self.question} (Ans-->{self.answer})'

class ScoreBoard(models.Model):
    course=models.ForeignKey(Course,on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=CASCADE)
    score=models.IntegerField()


    def __str__(self):
        return f'{self.course}---{self.user}---{self.score}'

#User Registration form

class CreateUserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

