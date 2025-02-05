from django import forms
from django.contrib.auth import get_user_model

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = get_user_model() # Garanti l'utilisation du modele utiliseur personnalisé(qu'il soit 'MyUser' ou 'User')
        fields = ['username','password']
        labels = {
            'username':'Entrez votre nom',
            'password':'Entrez votre mot de passe',
        }
        help_texts = { 'username':'' }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class RegistrationForm(forms.ModelForm):
    password_ = forms.CharField(
        min_length=8, required=True,
        label = 'Confirmez votre mot de passe',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    class Meta:
        model = get_user_model() # Garanti l'utilisation du modele utiliseur personnalisé(qu'il soit 'MyUser' ou 'User')
        fields = ['username','email','school','department','password']
        labels = {
            'username':'Entrez votre nom',
            'email':'Entrez votre adresse e-mail',
            'school':'Selectionnez votre établissement',
            'department':'Quel est votre département',
            'password':'Entrez votre mot de passe',
        }
        help_texts = { 'username':'' }
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Moins de 150 caractères','class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'school':forms.Select(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Minimun 8 caractères','class':'form-control'}),
        }