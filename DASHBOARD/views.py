from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.http import HttpResponse
# Pour l'exportation des donnees au format excel
import openpyxl
# Pour l'exportation des donnees au format pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def verify_string(chaine):
    char_in=False
    for char in chaine:
        if char in ['<','>','@','/','$','?','!','*']:
            char_in=True
            break
    return char_in

@login_required # Force l'utilisateur a se loguer pour acceder a son dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required # Force l'utilisateur a se loguer pour acceder a la vue des recherches de dossiers
def search(request):
    saisie=request.GET['search']
    if saisie != "" and len(saisie)<=3 and verify_string(saisie)==False:
        return render(request, 'search.html')
    else:
        return redirect('dashboard')
