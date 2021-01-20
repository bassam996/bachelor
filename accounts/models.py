from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator



MY_CHOICES = (
        ('الفرقة الأولى', 'الفرقة الأولى'),
        ('الفرقة الثانية', 'الفرقة الثانية'),
        ('الفرقة الثالثة', 'الفرقة الثالثة'),
        ('الفرقة الرابعة', 'الفرقة الرابعة'),
    )

MY_STATUS = (
        ('انتظام' , 'انتظام'),
        ('انتساب' , 'انتساب'),
    )

MY_REGULATION = (
        ('لائحة جديده' , 'لائحة جديدة'),
        ('لائحة قديمة' , 'لائحة قديمة'),
    )

class Profile(models.Model):
    user                  = models.OneToOneField(User , on_delete = models.CASCADE , null = True , blank = True)
    personal_image        = models.ImageField(upload_to = 'profile_images/' , blank = True , null = True , help_text = 'ارفع صوره خاصه بك إختيارياً')
    phone_regex           = RegexValidator(regex=r'^\+?1?\d{11}$', message="رقم الهاتف يجب أن يكون من 11 رقم و لا يبدأ برمز الدوله مثال 01200000000")
    phone_number          = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    select_your_year      = models.CharField(max_length = 20 , blank = True , null = True , choices=MY_CHOICES , help_text = "اختار الفرقة الخاصة بك")
    select_your_status    = models.CharField(max_length = 10 , blank = True , null = True , choices=MY_STATUS , help_text = "اختار الفرقة الخاصة بك")
    select_your_regulation = models.CharField(max_length = 12 , blank = True , null = True , choices=MY_REGULATION , help_text = "اختار اللائحة الخاصة بك")
    def __str__(self):
        return str(self.user)

@receiver(post_save , sender = User)
def create_user_profile(sender , instance , created , **kwargs ):
    if created :
        Profile.objects.create(user = instance)
