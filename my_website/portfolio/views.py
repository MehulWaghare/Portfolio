from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def project1(request):
    return render(request, 'project1.html')

def project2(request):
    return render(request, 'project2.html')

def project3(request):
    return render(request, 'project3.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=full_message,
                from_email=email,
                recipient_list=['your_email@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'contact.html')


def resume(request):
    return render(request, 'resume.html')