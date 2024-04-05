from django.db import models
from django.contrib.auth.models import AbstractUser
 

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Book(models.Model):
    bookname=models.CharField(max_length=100)
    bookdescription=models.CharField(max_length=100)
    bookauthor=models.CharField(max_length=100)
    bookprice=models.IntegerField()
    # available=models.BooleanField(null=True)

    def __str__(self):
        return self.bookname

    
