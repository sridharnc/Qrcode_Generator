from django.urls import path

from Qrcodeapp import views

app_name='QRCODEAPP'
urlpatterns = [
    path('',views.home,name='home'),
    path('qrcode_generator/',views.qrcode_generator,name='qrcode_generator'),
    path('contactus/',views.contactform,name='contactus'),
]
