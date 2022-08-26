from django.shortcuts import render,redirect
from .form import SignUpForm,ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/passwordmanage/password_reset.html'
    email_template_name = 'accounts/passwordmanage/password_reset_email.html'
    subject_template_name = 'accounts/passwordmanage/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url ='/'



def Logout_view(request):
	logout(request)
	messages.success(request,"vous etes deconnecter a votre compt merci !!!")
	return redirect('login-view')

def Login_View(request):
	if request.method=='POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)

	    if user is not None:
	        login(request, user)
	        return redirect('/')
	        ...
	    else:
	        messages.error(request,'Erreur de Connection a votre compt identifiant invalide !!!')
	        ...
	return render(request,'accounts/login.html',{})


def SignUp_View(request):


	if request.method=='POST':
		formsignup=SignUpForm(request.POST)
		fornProfile=ProfileForm(request.POST,request.FILES)

		if formsignup.is_valid() and fornProfile.is_valid():
			user=formsignup.save()
			profile=fornProfile.save(commit=False)
			profile.user=user
			profile.save()
			messages.success(request,"votre compt est bien cree connectez-vous")
			return redirect('login-view')
	else:
		formsignup=SignUpForm()
		fornProfile=ProfileForm()

	return render(request,'accounts/signup.html',{'formsignup':formsignup,'fornProfile':fornProfile})
			





