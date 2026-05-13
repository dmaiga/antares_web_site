from django.shortcuts import render
from django.views.generic import DetailView

from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.utils.translation import gettext_lazy as _


def home(request):
    context = {
        'clients': range(1, 16)
    }
    return render(request, 'site_web/home/home.html', context)

def about(request):
    return render(request, 'site_web/about/about.html')

def contact(request):
    return render(request, 'site_web/contact/contact.html')



def jobs(request):
    # Simulation d'une base de données pour la démo
    job_list = [
        {
            "title": _("Chef de Chantier Photovoltaïque"),
            "status": _("Nouveau"),
            "sector": _("Mines & Énergie"),
            "location": _("Kayes, Mali"),
            "contract": _("CDI"),
            "description": _(
                "Supervision des équipes d'installation et respect des normes "
                "de sécurité sur site industriel."
            ),
            "pub_date": _("22 Avr. 2026"),
            "deadline": _("10 Mai 2026"),
        },

        {
            "title": _("Analyste de Crédit Senior"),
            "status": _("Urgent"),
            "sector": _("Banque & Finance"),
            "location": _("Bamako, Mali"),
            "contract": _("CDI"),
            "description": _(
                "Analyse de risques financiers pour les comptes entreprises et "
                "structuration de dossiers."
            ),
            "pub_date": _("20 Avr. 2026"),
            "deadline": _("05 Mai 2026"),
        },

        {
            "title": _("Responsable Supply Chain"),
            "status": _("Fermé"),
            "sector": _("Logistique"),
            "location": _("Sikasso, Mali"),
            "contract": _("CDD"),
            "description": _(
                "Optimisation des flux de marchandises et gestion des entrepôts "
                "pour une multinationale."
            ),
            "pub_date": _("15 Avr. 2026"),
            "deadline": _("Expiré"),
        },

        {
            "title": _("Chargé de Recrutement IT"),
            "status": _("Ouvert"),
            "sector": _("Ressources Humaines"),
            "location": _("Bamako, Mali"),
            "contract": _("Intérim"),
            "description": _(
                "Sourcing et évaluation de profils développeurs et ingénieurs "
                "data."
            ),
            "pub_date": _("25 Avr. 2026"),
            "deadline": _("20 Mai 2026"),
        },

        {
            "title": _("Ingénieur Réseaux"),
            "status": _("Nouveau"),
            "sector": _("Télécoms"),
            "location": _("Bamako, Mali"),
            "contract": _("CDI"),
            "description": _(
                "Maintenance de l'infrastructure réseau fibre optique et "
                "sécurité."
            ),
            "pub_date": _("27 Avr. 2026"),
            "deadline": _("30 Mai 2026"),
        },
    ]

    context = {
        'jobs': job_list,
    }

    return render(
        request,
        'site_web/jobs/jobs.html',
        context
    )

from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class JobDetailView(TemplateView):
    template_name = 'site_web/jobs/detail_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs.get('slug')

        jobs_data = {
            'assistant-rh-polyvalent': {
                'title': _('Assistant RH Polyvalent'),
                'reference': 'ANT-RH-2026-01',
                'location': _('Bamako, Mali'),
                'contract': _('CDI'),
                'sector': _('Ressources Humaines'),
                'deadline': _('30 Juin 2026'),
                'email': 'recrutement@antares-rh.com',

                'main_mission': _(
                    "Assurer le suivi administratif RH et participer aux "
                    "activités de recrutement et de gestion du personnel."
                ),

                'responsibilities': [
                    _('Suivi administratif des dossiers du personnel'),
                    _('Publication des offres et présélection des candidatures'),
                    _('Organisation des entretiens'),
                    _('Participation au reporting RH'),
                ],

                'profile': [
                    _('Licence en Ressources Humaines ou équivalent'),
                    _('Première expérience en administration RH'),
                    _('Bonne maîtrise des outils bureautiques'),
                    _('Bonne communication écrite et orale'),
                ],

                'application': _(
                    "Envoyez votre CV et votre lettre de motivation à "
                    "l’adresse indiquée avant la date limite."
                ),
            },

            'assistant-comptable': {
                'title': _('Assistant Comptable'),
                'reference': 'ANT-FIN-2026-02',
                'location': _('Bamako, Mali'),
                'contract': _('CDD'),
                'sector': _('Finance & Comptabilité'),
                'deadline': _('12 Juillet 2026'),
                'email': 'recrutement@antares-rh.com',

                'main_mission': _(
                    "Participer au suivi comptable et au traitement des "
                    "opérations administratives courantes."
                ),

                'responsibilities': [
                    _('Saisie des pièces comptables'),
                    _('Classement et archivage des documents'),
                    _('Suivi des paiements et rapprochements'),
                    _('Appui aux opérations administratives'),
                ],

                'profile': [
                    _('Formation en comptabilité ou gestion'),
                    _('Bonne maîtrise d’Excel'),
                    _('Rigueur et sens de l’organisation'),
                ],

                'application': _(
                    "Merci de transmettre votre candidature complète avant "
                    "la date indiquée."
                ),
            },
        }

        job = jobs_data.get(slug)

        if not job:
            raise Http404(_("Cette offre n'existe pas."))

        context['job'] = job

        return context


def services(request):
    services = [
        {
            "title": _("Recrutement & Évaluation"),
            "description": _("Identification, sélection et évaluation de profils qualifiés selon les exigences techniques et organisationnelles de votre entreprise."),
            "icon": "user-group",
        },
        {
            "title": _("Intérim & Mise à disposition"),
            "description": _("Mise à disposition de personnel qualifié avec prise en charge administrative, sociale et contractuelle."),
            "icon": "clock",
        },
        {
            "title": _("Gestion Administrative RH"),
            "description": _("Gestion des contrats, paie, déclarations sociales et suivi administratif du personnel conformément à la réglementation malienne."),
            "icon": "document-check",
        },
        {
            "title": _("Conseil & Audit Social"),
            "description": _("Audit RH, conformité sociale, diagnostics organisationnels et accompagnement dans la structuration des procédures RH."),
            "icon": "briefcase",
        },
        {
            "title": _("Formation Professionnelle"),
            "description": _("Conception et animation de formations adaptées aux besoins opérationnels et au développement des compétences."),
            "icon": "academic-cap",
        },
        {
            "title": _("Sous-traitance & Appui Opérationnel"),
            "description": _("Gestion externalisée d’activités et d’équipes opérationnelles dans les domaines logistiques, administratifs et techniques."),
            "icon": "presentation-chart",
        },
    ]

    return render(
        request,
        'site_web/services/services.html',
        {'services': services}
    )




def espace_candidat(request):
    clients = range(1, 16)

    secteurs = sorted([
        _("Banque & Assurance"),
        _("BTP & Infrastructures"),
        _("Distribution & FMCG"),
        _("Grande Distribution"),
        _("Industrie Agroalimentaire"),
        _("Mines & Énergie"),
        _("Nettoyage & Facility Management"),
        _("ONG & Projets Internationaux"),
        _("Production Industrielle"),
        _("Services Externalisés"),
        _("Technologie & IT"),
        _("Télécommunications"),
        _("Transport & Logistique"),
    ])

    context = {
        "clients": clients,
        "secteurs": secteurs,
    }

    return render(
        request,
        'site_web/espaces/espace_candidat.html',
        context
    )


def espace_consultant(request):
    clients = range(1, 16)

    secteurs = sorted([
        _("Banque & Assurance"),
        _("BTP & Infrastructures"),
        _("Distribution & FMCG"),
        _("Grande Distribution"),
        _("Industrie Agroalimentaire"),
        _("Mines & Énergie"),
        _("Nettoyage & Facility Management"),
        _("ONG & Projets Internationaux"),
        _("Production Industrielle"),
        _("Services Externalisés"),
        _("Technologie & IT"),
        _("Télécommunications"),
        _("Transport & Logistique"),
    ])

    context = {
        "clients": clients,
        "secteurs": secteurs,
    }

    return render(
        request,
        'site_web/espaces/espace_consultant.html',
        context
    )


def espace_entreprise(request):

    clients = range(1, 16)

    secteurs = sorted([
        _("Banque & Assurance"),
        _("BTP & Infrastructures"),
        _("Distribution & FMCG"),
        _("Grande Distribution"),
        _("Industrie Agroalimentaire"),
        _("Mines & Énergie"),
        _("Nettoyage & Facility Management"),
        _("ONG & Projets Internationaux"),
        _("Production Industrielle"),
        _("Services Externalisés"),
        _("Technologie & IT"),
        _("Télécommunications"),
        _("Transport & Logistique"),
    ])

    services = [
        {
            "title": _("Recrutement & Évaluation"),
            "description": _(
                "Identification, sélection et évaluation de profils qualifiés "
                "selon les besoins techniques et organisationnels de votre entreprise."
            ),
            "highlight": _("Sélection rigoureuse"),
            "icon": "users",
        },

        {
            "title": _("Intérim & Mise à disposition"),
            "description": _(
                "Mise à disposition de personnel qualifié avec prise en charge "
                "administrative, sociale et contractuelle."
            ),
            "highlight": _("Gestion RH complète"),
            "icon": "briefcase",
        },

        {
            "title": _("Gestion Administrative RH"),
            "description": _(
                "Gestion des contrats, paie, déclarations sociales et suivi "
                "administratif du personnel conformément à la réglementation malienne."
            ),
            "highlight": _("Conformité sociale"),
            "icon": "building",
        },

        {
            "title": _("Conseil & Audit Social"),
            "description": _(
                "Audit RH, diagnostics organisationnels et accompagnement "
                "dans la structuration des procédures et pratiques RH."
            ),
            "highlight": _("Audit & conformité"),
            "icon": "shield",
        },

        {
            "title": _("Formation Professionnelle"),
            "description": _(
                "Conception et animation de formations adaptées aux besoins "
                "opérationnels et au développement des compétences."
            ),
            "highlight": _("Renforcement des capacités"),
            "icon": "graduation",
        },

        {
            "title": _("Sous-traitance & Appui Opérationnel"),
            "description": _(
                "Gestion externalisée d’activités et d’équipes opérationnelles "
                "dans les domaines logistiques, administratifs et techniques."
            ),
            "highlight": _("Flexibilité opérationnelle"),
            "icon": "layers",
        },
    ]

    context = {
        "clients": clients,
        "secteurs": secteurs,
        "services": services,
    }

    return render(
        request,
        "site_web/espaces/espace_entreprise.html",
        context
    )


def login_view(request):
   
    return render(request, 'site_web/auth/login.html')

def register_view(request):
    # Logique pour la redirection vers le formulaire d'enrôlement expert
    return render(request, 'site_web/auth/register.html')