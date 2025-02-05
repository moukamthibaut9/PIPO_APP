from django.shortcuts import render, redirect
from SIGN.forms import ConnexionForm, RegistrationForm
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from decouple import config
# Pour validation du compte par mail
import secrets
import uuid
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
#from django.contrib.sites.models import Site
from django.conf import settings

SEL=config('SEL')

def sign_up(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']==form.cleaned_data['password_']:
                for user in get_user_model().objects.all():
                    if form.cleaned_data['username']==user.username:
                        messages.error(request,"Le nom que vous avez entré est déjà pris")
                        return render(request,'sign_up.html',{'registration_form':form,})
                # Générer un token de validation
                token = str(uuid.uuid4())
                # Ajout du sel au mot de passe
                user_password=form.cleaned_data['password'][:-5]+SEL+form.cleaned_data['password'][-5:]
                # Création d'un utilisateur non vérifié
                user=get_user_model().objects.create_user(
                                            username=form.cleaned_data['username'], 
                                            email=form.cleaned_data['email'],
                                            school=form.cleaned_data['school'],
                                            department=form.cleaned_data['department'],
                                            password=user_password,
                                            email_verification_token = token)
                if user is not None:
                    ############ Envoi de l'email de validation #############
                    # Générer le lien d'activation
                    domain = get_current_site(request).domain
                    validation_url_name = 'sign/email_validation'
                    confirmation_link = f"http://{domain}/{validation_url_name}/{token}/"
                    subject = 'Confirmez votre adresse e-mail'
                    message = render_to_string('email_confirmation.html', {
                        'user': user,
                        'confirmation_link': confirmation_link,
                    })
                    # Envoyer l'email
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=message)
                    messages.success(request,"Un lien de confirmation de votre adresse vous a été envoyé. \
                                        Veillez ouvrir votre boîte et cliquez dessus avant de pouvoir vous connecter.")
                    return render(request,'sign_up.html',{'registration_form':form,})
                else:
                    messages.error(request,"Une problème est survenue durant le traitement de votre requête. Veillez reéssayer.")
                    return render(request,'sign_up.html',{'registration_form':form,})
            else:
                messages.error(request,"Vous avez entré deux mots de passe différents.")
                return render(request,'sign_up.html',{'registration_form':form,})    
            
        else:
            return render(request,'sign_up.html',{'registration_form':form,})
    form=RegistrationForm()
    return render(request,'sign_up.html',{'registration_form':form,})

def sign_in(request):
    if request.method=='POST':
        form=ConnexionForm(request.POST)
        if form.is_valid():
            user_password=form.cleaned_data['password'][:-5]+SEL+form.cleaned_data['password'][-5:]
            user=authenticate(username=form.cleaned_data['username'],password=user_password)
            if user is not None:
                if user.is_verified:
                    login(request,user)
                    return redirect('dashboard')
                else:
                    messages.error(request,"Vous n'avez pas encore validé votre adresse")
                    return render(request,'sign_in.html',{'connexion_form':form,})
            else:
                messages.error(request,"OUPS! La connexion a échouée. Vérifiez que vos informations sont correctes.")
                return render(request,'sign_in.html',{'connexion_form':form,})
        else:
            return render(request,'sign_in.html',{'connexion_form':form})
    form=ConnexionForm()
    return render(request,'sign_in.html',{'connexion_form':form,})
def sign_out(request):
    for user in get_user_model().objects.filter():
        logout(request)
    return redirect('home')

# Vue qui permet de valider l'utilisateur lorsqu'il clique sur le lien de validation dans sa boite mail
def email_validation(request, token):
    try:
        user = get_user_model().objects.get(email_verification_token=token)
        user.is_verified = True  # Authentifier l'utilisateur
        user.email_verification_token = ''  # Supprimer le token après validation
        user.save()
        return redirect('sign_in')  # Rediriger vers la page de connexion
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        get_user_model().objects.exclude(email_verification_token='').delete()
        messages.error(request,"La validation a echoué. Veillez vous enregistrer à nouveau.")
        messages.e
        return render(request,'sign_up.html')


# Relatif à la reinitialisation du mot de passe
class PasswordReset1(PasswordResetView):
    template_name = 'registration/password_reset1.html'
class PasswordReset2(PasswordResetDoneView):
    template_name = 'registration/password_reset2.html'
class PasswordReset3(PasswordResetConfirmView):
    template_name = 'registration/password_reset3.html'
class PasswordReset4(PasswordResetCompleteView):
    template_name = 'registration/password_reset4.html'
    
