from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact,Service,Pricing,Testmonial,Work,Blog
# Create your views here.
def index(request):
    return render(request, 'index.html')


def components(request):
    return render(request, "components.html")


def service(request):
    name = Service.objects.all()
    return render(request, "service.html", {'name': name})


def pricing(request):
    plans = Pricing.objects.all()
    return render(request, 'pricing.html', {'plans': plans})

def testmonial(request):
    test = Testmonial.objects.all()
    return render(request, "testmonial.html", {'test': test})

def contact(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["comment"]

        user = Contact(name=name,email=email,message=message)
        user.save()

        subject = "From Samundra"
        message = "Thank you for contacting me! \n I will contact u soon stay tuned"
        from_email = 'aaerik534@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email,recipient_list,fail_silently=False)

        messages.success(request,"Thank you for contacting me")
        
    return render(request, "contact.html")


def work(request):
    projects = Work.objects.all()
    return render(request, "works.html", {'projects' : projects})


def blog(request):
    posts = Blog.objects.all()
    return render(request, "blog.html", {'posts':posts})







