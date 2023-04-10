from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if not name or not email or not message:
            error = 'All fields are required.'
            return render(request, 'index.html', {'error': error})

        subject = 'New message from your portfolio website'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        sender_email = 'email'
        receiver_email = ['rahulkrishnan653@gmail.com']

        send_mail(subject, body, sender_email, receiver_email, fail_silently=False)

        message = 'Thank you for your message!'
        return render(request, 'index.html', {'message': message})

    return render(request, "index.html")
