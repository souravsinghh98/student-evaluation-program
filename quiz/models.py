from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name

class Question(models.Model):
    ques = models.TextField()
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100, null=True)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, null=True)
    option4 = models.CharField(max_length=100, null=True)
    correct = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ques

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    image = models.ImageField(upload_to='images/profile', null=True, default='images/profile/default.png', blank=True)
    
    def __str__(self):
        return self.user.first_name


