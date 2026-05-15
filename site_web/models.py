from django.db import models


class Enrolement(models.Model):

    TYPE_PROFIL_CHOICES = [
        ('candidat', 'Candidat'),
        ('consultant', 'Consultant'),
        ('entreprise', 'Entreprise'),
    ]

    type_profil = models.CharField(
        max_length=20,
        choices=TYPE_PROFIL_CHOICES
    )

    nom = models.CharField(
        max_length=100
    )

    prenom = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    telephone = models.CharField(
        max_length=30
    )

    entreprise = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    poste = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    secteur_activite = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    cv = models.FileField(
        upload_to='enrolements/cv/',
        blank=True,
        null=True
    )

    dossier_examine = models.BooleanField(
        default=False
    )

    dossier_valide = models.BooleanField(
        default=False
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Enrôlement"
        verbose_name_plural = "Enrôlements"

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.type_profil}"