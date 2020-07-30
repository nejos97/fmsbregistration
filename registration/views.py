from django.shortcuts import render, get_object_or_404, redirect
from registration.utils import get_random_string
from registration.utils import generate_pdf
from registration.models import Dossier
from django_xhtml2pdf.utils import pdf_decorator

# Create your views here.
def home(request):
    return render(request, "home.html")

def start(request):
    context = {}
    dossier = Dossier()
    dossier.save()
    context["dossier"] = dossier

    return render(request, "start.html", context)

def step_one(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)

    if request.method=="POST":

        nom_complet = request.POST['nom_complet']
        date_naissance = request.POST['date_naissance']
        lieu_naissance = request.POST['lieu_naissance']
        sexe = request.POST['sexe']
        nationalite = request.POST['nationalite']
        region_origine = request.POST['region_origine']
        departement_origine = request.POST['departement_origine']

        dossier.nom_complet = nom_complet
        dossier.date_naissance = date_naissance
        dossier.lieu_naissance = lieu_naissance
        dossier.sexe = sexe
        dossier.nationalite = nationalite
        dossier.region_origine = region_origine
        dossier.departement_origine = departement_origine
        dossier.save()

        return redirect('registration:step_two', token=token)



    context["dossier"] = dossier
    return render(request, "step_one.html", context)

def step_two(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)
    
    if request.method=="POST":
        #recuperation des information
        filiere_choisie = request.POST['filiere_choisie']
        centre_examen = request.POST['centre_examen']
        annee_bac = request.POST['annee_bac']
        mention_bac = request.POST['mention_bac']
        annee_probatoire = request.POST['annee_probatoire']
        mention_probatoire = request.POST['mention_probatoire']

        #mise a jour des donnee recu
        dossier.filiere_choisie = filiere_choisie
        dossier.centre_examen = centre_examen
        dossier.annee_bac = annee_bac
        dossier.mention_bac = mention_bac
        dossier.annee_probatoire = annee_probatoire
        dossier.mention_probatoire = mention_probatoire
        dossier.save()
        
        #redirection a la page suivant
        return redirect('registration:step_three', token=token)

    context["dossier"] = dossier
    return render(request, "step_two.html", context)

def step_three(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)
    if request.method=="POST":
        dossier.photocopie_bac = request.FILES.get('photocopie_bac')
        dossier.photocopie_releve_note_bac = request.FILES.get('photocopie_releve_note_bac')
        dossier.photocopie_releve_note_probatoire = request.FILES.get('photocopie_releve_note_probatoire')
        dossier.save()
        return redirect('registration:step_four', token=token)

    context["dossier"] = dossier
    return render(request, "step_three.html", context)

def step_four(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)
    if request.method=="POST":
        dossier.recu_paiement = request.FILES.get('recu_paiement')
        dossier.save()
        return redirect('registration:step_five', token=token)

    context["dossier"] = dossier
    return render(request, "step_four.html", context)

def step_five(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)

    if request.method=="POST":
        dossier.photocopie_acte_naissance = request.FILES.get('photocopie_acte_naissance')
        dossier.certificat_medical = request.FILES.get('certificat_medical')
        dossier.photo_4x4 = request.FILES.get('photo_4x4')
        return redirect('registration:end', token=token)

    context["dossier"] = dossier
    return render(request, "step_five.html", context)

def end(request, token):
    context = {}
    dossier = get_object_or_404(Dossier, token=token)
    context["dossier"] = dossier
    return render(request, "end.html", context)

def delete(request):
    context = {}
    if request.method == "POST":
        context["process"] = True 
        code = request.POST['code']
        dossier = Dossier.objects.filter(code=code).first()

        if dossier != None:
            dossier.delete = True
            dossier.save()            
        context['dossier'] = dossier
    return render(request, "delete.html", context)

def download(request):
    context = {}
    if request.method == "POST":
        context["process"] = True 
        code = request.POST['code']
        dossier = Dossier.objects.filter(code=code).first()
        if dossier != None:
            return redirect('registration:download_recip', token=dossier.token)           
        context['dossier'] = dossier
    return render(request, "download.html", context)

@pdf_decorator(pdfname='recepisse_candidat.pdf')
def download_recip(request, token):
    context = {}
    context['dossier'] = dossier = Dossier.objects.filter(token=token).first()
    return render(request, 'pdf/recepisse.html', context)
    
