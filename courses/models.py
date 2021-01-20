from django.db import models
from datetime import datetime
from import_export.admin import ImportExportModelAdmin


# Create your models here.

class FirstYear(models.Model):
    name = models.CharField(max_length = 50 , null = True , blank = True)
    name_en = models.CharField(max_length = 50 , null = True , blank = True)
    image = models.ImageField(upload_to = 'first_year_images/' , null = True , blank = True)
    desc = models.TextField(null = True , blank = True)
    desc_en = models.TextField(null = True , blank = True)
    Price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class SecondYear(models.Model):
    name = models.CharField(max_length = 50 , null = True , blank = True)
    name_en = models.CharField(max_length = 50 , null = True , blank = True)
    image = models.ImageField(upload_to = 'second_year_images/' , null = True , blank = True)
    desc = models.TextField(null = True , blank = True)
    desc_en = models.TextField(null = True , blank = True)
    Price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class ThirdYear(models.Model):
    name = models.CharField(max_length = 50 , null = True , blank = True)
    name_en = models.CharField(max_length = 50 , null = True , blank = True)
    image = models.ImageField(upload_to = 'third_year_images/' , null = True , blank = True)
    desc = models.TextField(null = True , blank = True)
    desc_en = models.TextField(null = True , blank = True)
    Price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class ForthYear(models.Model):
    name = models.CharField(max_length = 50 , null = True , blank = True)
    name_en = models.CharField(max_length = 50 , null = True , blank = True)
    image = models.ImageField(upload_to = 'forth_year_images/' , null = True , blank = True)
    desc = models.TextField(null = True , blank = True)
    desc_en = models.TextField(null = True , blank = True)
    Price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class BuyConfirmation(models.Model):
    firstyear     = models.ForeignKey(FirstYear , on_delete= models.CASCADE , null = True , blank = True )
    secondyear    = models.ForeignKey(SecondYear , on_delete = models.CASCADE , null = True , blank = True)
    thirdyear     = models.ForeignKey(ThirdYear , on_delete = models.CASCADE , null = True , blank = True)
    forthyear     = models.ForeignKey(ForthYear , on_delete = models.CASCADE , null = True , blank = True )
    fullname      = models.CharField(max_length = 100 , verbose_name = "اكتب اسمك بالكامل")
    receiptnumber = models.CharField(max_length = 1000 , verbose_name = "اكتب رقم إيصال الدفع")
    gmailaccount  = models.EmailField(verbose_name = "اكتب الچيميل الخاص بجوجل درايڤ")
    Paid_NotPaid  = models.BooleanField(default = False , null = True , blank = True)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.receiptnumber
