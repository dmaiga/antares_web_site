from django.contrib import admin

from .models import Enrolement


@admin.register(Enrolement)
class EnrolementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_complet',
        'type_profil',
        'email',
        'telephone',
        'entreprise',
        'dossier_examine',
        'dossier_valide',
        'date_creation',
    )

    list_filter = (
        'type_profil',
        'dossier_examine',
        'dossier_valide',
        'date_creation',
    )

    search_fields = (
        'nom',
        'prenom',
        'email',
        'telephone',
        'entreprise',
    )

    readonly_fields = (
        'date_creation',
    )

    ordering = (
        '-date_creation',
    )

    list_per_page = 25

    fieldsets = (

        (
            'Informations générales',
            {
                'fields': (
                    'type_profil',
                    'nom',
                    'prenom',
                    'email',
                    'telephone',
                )
            }
        ),

        (
            'Informations entreprise',
            {
                'fields': (
                    'entreprise',
                    'secteur_activite',
                    'poste',
                )
            }
        ),

        (
            'Consultant',
            {
                'fields': (
                    'cv',
                )
            }
        ),

        (
            'Validation dossier',
            {
                'fields': (
                    'dossier_examine',
                    'dossier_valide',
                )
            }
        ),

        (
            'Métadonnées',
            {
                'fields': (
                    'date_creation',
                )
            }
        ),
    )

    def nom_complet(self, obj):

        return f"{obj.prenom} {obj.nom}"

    nom_complet.short_description = (
        'Nom complet'
    )