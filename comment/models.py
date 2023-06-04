from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager
# Create your models here.


class Question (models.Model):
    questions = models.CharField(max_length = 10000)
    name = models.CharField( max_length=50)
    date = models.DateTimeField (default= datetime.now , blank=True)
    tags = TaggableManager()
    def __str__(self):
        return self.questions
    
class Answer (models.Model):
    question = models.ForeignKey(Question,related_name='Question_Answer',on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    answer = models.TextField(max_length = 10000)
    date = models.DateTimeField (default= datetime.now , blank=True)
    
    def __str__(self):
        return self.answer
    
