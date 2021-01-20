from django import forms
from .models import BuyConfirmation

class BuyConfirmationForm(forms.ModelForm):
    class Meta :
        model = BuyConfirmation
        fields = ['fullname' , 'receiptnumber' , 'gmailaccount' ]
