from django.shortcuts import render
from . models import PostContent
import smtplib

# Create your views here.
def submit(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        mob=request.POST.get("mobile")
        message=request.POST.get("message")

        print(name," ",email," ",mob," ",message)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login("your_email", "your_password")

        message_text = "Person Details who wants to contact with us :  Name     email id     mobile number   message \n"+name+"\t\t"+email+"\t\t"+mob+"\t\t"+message

        s.sendmail("senders_mail_id", "receivers_mail_id", message_text)

        s.quit()

        par={'msg':'Thanks for get in touch with amalgusbiotech.com'}

        return render(request,'contactus.html',par)

    else:
        return render(request,'landingpage.html')


def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

def home(request):
    posts=PostContent.objects.order_by('-date')[:3]
    return render(request,'landingpage.html',{'posts':posts})

def home1(request):
    posts=PostContent.objects.order_by('-date')[:3]
    return render(request,'landingpage.html',{'posts':posts})

def login(request):
    return render(request,'login.html')

def products(request):
    return render(request,'products.html')

def blog(request):
    posts=PostContent.objects.order_by('-date')[0:]
    return render(request,'blogpage.html',{'posts':posts})
