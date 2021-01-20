from django.shortcuts import render , redirect
from .forms import SignUpForm , UserProfileEditForm , ProfileEditForm
from django.contrib.auth import authenticate , login
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            messages.success(request, 'تم التسجيل بنجاح يرجى إكمال بيانات ملفك الشخصي ')
            return redirect('/accounts/profile')
    else :
        form = SignUpForm()
        customizeform = ProfileEditForm()
    context = {'form' : form }
    return render(request , 'registration/signup.html' , context )



# Profile View Def

@login_required
def profile_view(request):
    private_profile = Profile.objects.get(user = request.user)
    context = {'pr_profile' : private_profile }
    return render(request , 'profile.html' , context)



# Edit Profile Def

@login_required
def profile_edit(request):
    private_profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        usform = UserProfileEditForm(request.POST , instance = request.user)
        prform = ProfileEditForm(request.POST , request.FILES , instance = private_profile)
        if usform.is_valid() and prform.is_valid():
            usform.save() and prform.save(commit = False)
            prform.user = request.user
            prform.save()
            messages.success(request, 'تم تعديل صفحتك الشخصية بنجاح !!!')
            return redirect('/accounts/profile')

    else :
        usform = UserProfileEditForm(instance = request.user)
        prform = ProfileEditForm(instance = private_profile)
    context = {'prform' : prform , 'usform' : usform }
    return render(request , 'profile_edit.html' , context)
