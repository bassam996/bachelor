from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 30 , null = True , blank = False)
    phone = models.CharField(max_length = 11 , null = True , blank = False)
    email = models.EmailField(null = True , blank = False)
    message = models.TextField(null = True , blank = False)
