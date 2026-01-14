from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from django.conf import settings
import os
from django.core.mail import send_mail


#function for home 
def home(request):
    return render(request,'index.html')

#function for contact form
def contactform(request):
    msg = None
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["sridharchakkaravarthy1@gmail.com"],  # replace with your email
        )

        msg = "Message sent successfully!"

    return render(request, "contact.html", {"msg": msg})


#function for qrgeneratorpage and creating
def qrcode_generator(request):
    if request.method == 'POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            NAME=form.cleaned_data['name'];
            URL=form.cleaned_data['url'];
            QRCODE=qrcode.make(URL)
            File_name=NAME.replace(" ","_").lower()+'_menu.png'
            filepath=os.path.join(settings.MEDIA_ROOT,File_name)
            QRCODE.save(filepath)

            # creating image url
            qrurl=os.path.join(settings.MEDIA_URL,File_name)
            
            context={
                'NAME':NAME,
                'qrurl':qrurl,
                'filename':File_name
            }
            return render(request,"result_QrGenerator.html",context)
    else:
        form=QRCodeForm()
        context={
            'form':form
        }
        return render(request,'Qrcode_generator.html',context)
