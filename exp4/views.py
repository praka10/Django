from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

from django.conf import settings
from django.shortcuts import render

def send_email(request):

    send_mail(
        'Welcome Party - reg.',
        'Greetings!!! Welcome to the Department of Information Technology.',
        settings.EMAIL_HOST_USER,
        ['22uit084@kamarajengg.edu.in'],
        fail_silently=False,
    )

    return render(request, 'sendMail.html')