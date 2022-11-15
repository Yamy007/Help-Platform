from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from .tokens import account_activation_token


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message = render_to_string("template_activate_account.html", {
        'user':user.username,
        'domain':get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request,f"hi , {user} please activate email {to_email}")
    else:
         messages.error(request, f"problem sending email to {to_email}, check if you typed it correctly")
    
def activate(request, uidb64, token):
    return redirect('/')



def register(request):

    if request.method != 'POST':

        form = UserRegistrationForm()
    else:
   
        form = UserRegistrationForm(data=request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
