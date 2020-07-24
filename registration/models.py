from django.db import models
import uuid
from registration.utils import get_random_string
# Create your models here.

class Dossier(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=200, default=get_random_string)
    nom_complet = models.CharField(max_length=200, blank=True)
    date_naissance = models.DateField(blank=True, null=True )
    lieu_naissance = models.CharField(max_length=200, blank=True, null=True)
    sexe = models.CharField(max_length=200, blank=True, null=True)
    nationalite = models.CharField(max_length=200, blank=True, null=True)
    region_origine = models.CharField(max_length=200, blank=True, null=True)
    departement_origine = models.CharField(max_length=200, blank=True, null=True)
    filiere_choisie = models.CharField(max_length=200, blank=True, null=True)
    centre_examen = models.CharField(max_length=200, blank=True, null=True)
    annee_probatoire = models.IntegerField(blank=True, null=True)
    mention_probatoire = models.CharField(max_length=200, blank=True, null=True)
    annee_bac = models.IntegerField(blank=True,null=True)
    mention_bac = models.CharField(max_length=200, blank=True, null=True)
    photocopie_bac = models.CharField(max_length=200, blank=True, null=True)
    photocopie_releve_note_bac = models.CharField(max_length=200, blank=True, null=True)
    photocopie_releve_note_probatoire = models.CharField(max_length=200, blank=True, null=True)
    recu_paiement = models.CharField(max_length=200, blank=True, null=True)
    photocopie_acte_naissance = models.CharField(max_length=200, blank=True, null=True)
    certificat_medical = models.CharField(max_length=200, blank=True, null=True)
    photo_4x4 = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default= False, blank=True, null=True)
    delete = models.BooleanField(default= False, null=True)
    date_ajout = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    date_modification = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)


