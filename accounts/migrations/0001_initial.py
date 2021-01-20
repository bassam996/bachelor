# Generated by Django 3.1.5 on 2021-01-13 15:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_image', models.ImageField(blank=True, help_text='ارفع صوره خاصه بك إختيارياً', null=True, upload_to='profile_images/')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='رقم الهاتف يجب أن يكون من 11 رقم و لا يبدأ برمز الدوله مثال 01200000000', regex='^\\+?1?\\d{11}$')])),
                ('select_your_year', models.CharField(blank=True, choices=[('الفرقة الأولى', 'الفرقة الأولى'), ('الفرقة الثانية', 'الفرقة الثانية'), ('الفرقة الثالثة', 'الفرقة الثالثة'), ('الفرقة الرابعة', 'الفرقة الرابعة')], help_text='اختار الفرقة الخاصة بك', max_length=20, null=True)),
                ('select_your_status', models.CharField(blank=True, choices=[('انتظام', 'انتظام'), ('انتساب', 'انتساب')], help_text='اختار الفرقة الخاصة بك', max_length=10, null=True)),
                ('select_your_regulation', models.CharField(blank=True, choices=[('لائحة جديده', 'لائحة جديدة'), ('لائحة قديمة', 'لائحة قديمة')], help_text='اختار اللائحة الخاصة بك', max_length=12, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
