from django.urls import path
from . import views

app_name = 'courses'


urlpatterns = [
    path('', views.home , name = 'home'),
    path('firstyear', views.firstyear , name = 'firstyear'),
    path('firstyear/<int:id>', views.firstyeardetails , name = 'firstyeardetails'),
    path('secondyear', views.secondyear , name = 'secondyear'),
    path('secondyear/<int:id>', views.secondyeardetails , name = 'secondyeardetails'),
    path('thirdyear', views.thirdyear , name = 'thirdyear'),
    path('thirdyear/<int:id>', views.thirdyeardetails , name = 'thirdyeardetails'),
    path('forthyear', views.forthyear , name = 'forthyear'),
    path('forthyear/<int:id>', views.forthyeardetails , name = 'forthyeardetails'),
]
