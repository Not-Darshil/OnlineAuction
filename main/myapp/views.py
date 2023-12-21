from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import UserRegistrationForm, LoginForm

#authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .decorators import user_not_authenticated

#for authenticating through email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token

# Create your views here.

def activate(request, uidb64, token):
    return redirect('homepage')

def home(request):
    return render(request,'myapp/home.html')

def homepage(request):
    # return HttpResponse("request")
    return render(request,'myapp/homepage.html')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

@user_not_authenticated 
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="myapp/register.html",
        # template_name="users/register.html",
        context={"UserRegistrationForm": form}
        )






# def register(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect ("my_login")
    
    
#     context={'registerform':form}
#     return render(request,'myapp/register.html',context=context)


def my_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect ("dashboard")
    context={'loginform':form}

    return render(request,'myapp/my_login.html',context=context)


def user_logout(request):
    auth.logout(request)    
    return redirect("")


# @login_required(login_url="my_login") # for protecting the view of dashboard called as csrf protection
def dashboard(request):
    return render(request,'myapp/dashboard.html')


