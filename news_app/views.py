from django.shortcuts import render,redirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Data
from django.core.mail import send_mail
from django.utils.html import strip_tags
from datetime import datetime , timedelta

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from django.db import IntegrityError
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

def Inputs(request):
    if request.method=='POST':
        title=request.POST.get('title')
        contact=request.POST.get('contact')
        catagory=request.POST.get('category')
        date=request.POST.get('created_at')
        image=request.FILES.get('image')

        input_data=Data(
            title=title,
            contact=contact,
            catagory=catagory,
            date=date,
            image=image,
        )
        input_data.save()
        return redirect('front')
    return render(request,'upload.html')   
def Front(request):
    data = Data.objects.all()
    
    
    return render(request,'front.html',{'data':data})


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if username and password and email:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                try:
                    # Send confirmation email
                    html_content = render_to_string('email_template.html', {
                        'email': email,
                        'username': username,
                    })
                    text_content = f"{email}\n\n{username}"

                    email_msg = EmailMultiAlternatives(
                        subject="Welcome to our platform!",
                        body=text_content,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[email]  # Send to user's actual email
                    )
                    email_msg.attach_alternative(html_content, "text/html")
                    email_msg.send()

                    # Create the user
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, "Registration successful. Please login.")
                    return redirect('login')

                except Exception as e:
                    messages.error(request, f"Email sending failed: {str(e)}")
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'register.html')

def delete(request,Id):
    
    data = get_object_or_404(Data, id=Id)
    data.delete()
    return redirect('front') 


def update(request, id):
    data = get_object_or_404(Data, id=id)

    if request.method == 'POST':
        data.title = request.POST.get('title')
        data.catagory = request.POST.get('catagory')
        data.content = request.POST.get('content')
        data.steps = request.POST.get('steps')
        data.difficulty = request.POST.get('difficulty')
        
        # Only update image if a new one was provided
        if 'image' in request.FILES:
            data.image = request.FILES.get('image')
        
        data.save()
        return redirect('front')
    
    return render(request, 'update.html', {"data": data})   

        




def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('front')  # Change to your dashboard or homepage
        else:
            messages.error(request, "Invalid credentials")
            


    return render(request, 'login.html')
         
    