from django.shortcuts import render , redirect
from .models import FirstYear , SecondYear , ThirdYear , ForthYear
from .forms import BuyConfirmationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request ,'index.html')



# Def First Year Courses

@login_required
def firstyear(request):
    first_year_view = FirstYear.objects.all()
    context = {'first_year_context' : first_year_view }
    return render(request , 'first_year.html' , context)

@login_required
def firstyeardetails(request , id ):
    first_year_details = FirstYear.objects.get(id=id)
    if request.method == "POST":
        form = BuyConfirmationForm(request.POST)
        if form.is_valid():
            newform = form.save(commit = False)
            newform.firstyear = first_year_details
            newform.save()
            messages.success(request, 'تم إستقبال البيانات و سيتم مراجعتها , يرجى متابعة ملفاتك على درايڤ ')
            return redirect('/')

    else :
        form = BuyConfirmationForm()

    context = {'first_year_details' : first_year_details , 'form' : form }
    return render(request , 'first_details.html' , context)

# Def Second Year Courses


@login_required
def secondyear(request):
    second_year_view = SecondYear.objects.all()
    context = {'second_year_context' : second_year_view }
    return render(request , 'second_year.html' , context)

@login_required

def secondyeardetails(request , id):
    second_year_details = SecondYear.objects.get(id=id)
    if request.method == "POST":
        form = BuyConfirmationForm(request.POST)
        if form.is_valid():
            newform = form.save(commit = False)
            newform.secondyear = second_year_details
            newform.save()
            messages.success(request, 'تم إستقبال البيانات و سيتم مراجعتها , يرجى متابعة ملفاتك على درايڤ ')
            return redirect('/')
    else :
        form = BuyConfirmationForm()
    context = {'second_year_details' : second_year_details , 'form' : form }
    return render(request , 'second_details.html' , context )



# Def Third Year Courses


@login_required
def thirdyear(request):
    third_year_view = ThirdYear.objects.all()
    context = {'third_year_context' : third_year_view }
    return render(request , 'third_year.html' , context)

@login_required
def thirdyeardetails(request , id ):
    third_year_details = ThirdYear.objects.get(id=id)
    if request.method == "POST":
        form = BuyConfirmationForm(request.POST)
        if form.is_valid():
            newform = form.save(commit = False)
            newform.thirdyear = third_year_details
            newform.save()
            messages.success(request, 'تم إستقبال البيانات و سيتم مراجعتها , يرجى متابعة ملفاتك على درايڤ ')
            return redirect('/')
    else :
        form = BuyConfirmationForm()
    context = {'third_year_details' : third_year_details , 'form' : form }
    return render(request, 'third_details.html' , context)


# Def Forth Year Courses


@login_required
def forthyear(request):
    forth_year_view = ForthYear.objects.all()
    context = {'forth_year_context' : forth_year_view }
    return render(request , 'forth_year.html' , context)

@login_required
def forthyeardetails(request , id ):
    forth_year_details = ForthYear.objects.get(id=id)
    if request.method == "POST":
        form = BuyConfirmationForm(request.POST)
        if form.is_valid():
            newform = form.save(commit = False)
            newform.forthyear = forth_year_details
            newform.save()
            messages.success(request, 'تم إستقبال البيانات و سيتم مراجعتها , يرجى متابعة ملفاتك على درايڤ ')
            return redirect('/')
    else :
        form = BuyConfirmationForm()
    context = {'forth_year_details' : forth_year_details , 'form' : form }
    return render(request, 'forth_details.html' , context)
