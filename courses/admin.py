from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import BuyConfirmationResources


# Register your models here.

class BuyConfirmationAdmin(ImportExportModelAdmin):
    list_display = ['fullname' , 'receiptnumber' , 'gmailaccount' , 'Paid_NotPaid']
    list_filter = ['Paid_NotPaid' , 'firstyear' , 'secondyear' , 'thirdyear' , 'forthyear']
    search_fields = ['fullname' , 'receiptnumber' , 'gmailaccount']
    resource_class = BuyConfirmationResources

admin.site.register(BuyConfirmation , BuyConfirmationAdmin)

admin.site.register(FirstYear)
admin.site.register(SecondYear)
admin.site.register(ThirdYear)
admin.site.register(ForthYear)




admin.site.site_header = "Bachelor Administration"
admin.site.site_title = 'Bachelor Administration'
