from django.db import models
from django import forms

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    ucomment=models.TextField(max_length=1000)

class comment(models.Model):
    STATUS=(
        ('New','New'),
        ('True', 'True'),
        ('False','False')
    )
   
    
    
    name1 = models.CharField(max_length=70)
    
    subject=models.CharField(max_length=50,blank=True)
    comment1=models.CharField(max_length=250,blank=True)
    rate=models.IntegerField(default=1)
    ip=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['subject','comment1','rate']