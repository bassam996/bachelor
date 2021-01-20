from django.shortcuts import render , redirect
from .models import Contact
from django.contrib import messages


# Create your views here.

def contact(request):
    if request.method == "POST":
        x = request.POST.get('name')
        y = request.POST.get('phone')
        z = request.POST.get('email')
        t = request.POST.get('text')
        data = Contact(name = x , phone = y , email = z , message = t)
        data.save()
        messages.success(request, 'تم إستقبال رسالتك و سيتم التواصل معك قريباً ')
        return redirect('/')
    return render(request , 'contact.html')
