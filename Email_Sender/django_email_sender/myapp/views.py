from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name, # title or Subject
            message, # message
            'settings.EMAIL_HOST_USER', #sender if not available considered the default or configured
            [email], # receiver email
            fail_silently=False,
        )
    return render(request, 'index.html')