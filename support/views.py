from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from accounts.views import login
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.shortcuts import redirect, render


@login_required(login_url=login)
def send_email(request):

    if request.method == 'POST':

        user=request.user
        email = user.email

        current_site = get_current_site(request)
        mail_subject = 'Support will reach out to you'
        message = render_to_string('support/email_support.html',{

            'user':user,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)), #this encodes the user id 
            'token': default_token_generator.make_token(user), #and then a token is generated next to the user id

            })


        send_email = EmailMessage(mail_subject,message,to=[email])
        send_email.send()
        messages.success(request,'Thank You for reaching out !')
        return redirect('home')
    
    return render(request, 'support/mail_view.html')

    