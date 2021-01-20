from import_export import resources
from .models import BuyConfirmation

class BuyConfirmationResources(resources.ModelResource):
    class Meta :
        model = BuyConfirmation
        fields = ['gmailaccount']
