from django.shortcuts import render
from django.views.generic import DetailView

from django.views.generic import TemplateView
from django.http import Http404

def home(request):
    context = {
        'clients': range(1, 16)
    }
    return render(request, 'site_web/home/home.html', context)

def about(request):
    return render(request, 'site_web/about/about.html')

def contact(request):
    return render(request, 'site_web/contact/contact.html')

from django.shortcuts import render

def jobs(request):
    # Simulation d'une base de données pour la démo
    job_list = [
        {
            "title": "Chef de Chantier Photovoltaïque",
            "status": "Nouveau",
            "sector": "Mines & Énergie",
            "location": "Kayes, Mali",
            "contract": "CDI",
            "description": "Supervision des équipes d'installation et respect des normes de sécurité sur site industriel.",
            "pub_date": "22 Avr. 2026",
            "deadline": "10 Mai 2026",
        },
        {
            "title": "Analyste de Crédit Senior",
            "status": "Urgent",
            "sector": "Banque & Finance",
            "location": "Bamako, Mali",
            "contract": "CDI",
            "description": "Analyse de risques financiers pour les comptes entreprises et structuration de dossiers.",
            "pub_date": "20 Avr. 2026",
            "deadline": "05 Mai 2026",
        },
        {
            "title": "Responsable Supply Chain",
            "status": "Fermé",
            "sector": "Logistique",
            "location": "Sikasso, Mali",
            "contract": "CDD",
            "description": "Optimisation des flux de marchandises et gestion des entrepôts pour une multinationale.",
            "pub_date": "15 Avr. 2026",
            "deadline": "Expiré",
        },
        {
            "title": "Chargé de Recrutement IT",
            "status": "Ouvert",
            "sector": "Ressources Humaines",
            "location": "Bamako, Mali",
            "contract": "Intérim",
            "description": "Sourcing et évaluation de profils développeurs et ingénieurs data.",
            "pub_date": "25 Avr. 2026",
            "deadline": "20 Mai 2026",
        },
        {
            "title": "Ingénieur Réseaux",
            "status": "Nouveau",
            "sector": "Télécoms",
            "location": "Bamako, Mali",
            "contract": "CDI",
            "description": "Maintenance de l'infrastructure réseau fibre optique et sécurité.",
            "pub_date": "27 Avr. 2026",
            "deadline": "30 Mai 2026",
        },
    ]

    context = {
        'jobs': job_list,
    }
    
    return render(request, 'site_web/jobs/jobs.html', context)


class JobDetailView(TemplateView):
    template_name = 'site_web/jobs/detail_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')

        # Simulation d'une base de données Antarès
        jobs_data = {
            'assistant-rh-polyvalent': {
                'title': 'Assistant RH Polyvalent',
                'reference': 'ANT/00270125AF',
                'deadline': '27 Février 2025',
                'email': 'antares.ml@gmail.com',

                'main_mission': """
                Assister le service RH dans l’administration du personnel, le recrutement,
                la formation et l’évaluation du personnel.
                """,

                'description_html': """
                <h1>Recrutement :</h1>
                <ul>
                    <li>Analyser les besoins en recrutement</li>
                    <li>Rédiger fiches de poste et annonces</li>
                    <li>Faire le tri des CV et élaborer les grilles d’évaluation</li>
                    <li>Organiser et conduire des entretiens (individuels, collectifs, téléphoniques)</li>
                    <li>Proposer une sélection de candidats</li>
                    <li>Accompagner les nouveaux recrutés</li>
                </ul>



                
                """,

                'profile_html': """
                <ul>
                    <li>Licence en Ressources Humaines, Administration ou équivalent</li>
                    <li>Minimum 2 ans d’expérience</li>
                    <li>Maîtrise du droit du travail et des outils bureautiques</li>
                    <li>Bonnes capacités rédactionnelles et relationnelles</li>

                </ul>
                """,

                'application_html': """
                <p>
                Merci de transmettre votre <strong>CV détaillé</strong> et votre 
                <strong>lettre de motivation</strong> au plus tard le 
                <strong>27 Février 2025</strong> à l’adresse suivante :
                </p>

                <p class="font-bold">antares.ml@gmail.com</p>

                <p>
                Merci de mentionner la référence 
                <strong>ANT/ARHP/00270125AF</strong> en objet.
                </p>

                <p class="text-sm text-slate-500 mt-2">
                NB : seuls les candidats présélectionnés seront contactés.
                </p>
                """
            }
        }
        # Récupération de l'offre ou erreur 404
        job = jobs_data.get(slug)
        if not job:
            raise Http404("Cette offre n'existe pas.")

        context['job'] = job
        return context

def services(request):
   services = [
                    {
                        "title": "Recrutement & Évaluation",
                        "description": "Identification, sélection et évaluation de profils qualifiés selon les exigences techniques et organisationnelles de votre entreprise.",
                        "icon": "user-group",
                    },
                    {
                        "title": "Intérim & Mise à disposition",
                        "description": "Mise à disposition de personnel qualifié avec prise en charge administrative, sociale et contractuelle.",
                        "icon": "clock",
                    },
                    {
                        "title": "Gestion Administrative RH",
                        "description": "Gestion des contrats, paie, déclarations sociales et suivi administratif du personnel conformément à la réglementation malienne.",
                        "icon": "document-check",
                    },
                    {
                        "title": "Conseil & Audit Social",
                        "description": "Audit RH, conformité sociale, diagnostics organisationnels et accompagnement dans la structuration des procédures RH.",
                        "icon": "briefcase",
                    },
                    {
                        "title": "Formation Professionnelle",
                        "description": "Conception et animation de formations adaptées aux besoins opérationnels et au développement des compétences.",
                        "icon": "academic-cap",
                    },
                    {
                        "title": "Sous-traitance & Appui Opérationnel",
                        "description": "Gestion externalisée d’activités et d’équipes opérationnelles dans les domaines logistiques, administratifs et techniques.",
                        "icon": "presentation-chart",
                    },
                ]
   return render(request, 'site_web/services/services.html', {'services': services})



def espace_candidat(request):
    clients = range(1, 16)

    secteurs = sorted([
        "Banque & Assurance",
        "BTP & Infrastructures",
        "Distribution & FMCG",
        "Grande Distribution",
        "Industrie Agroalimentaire",
        "Mines & Énergie",
        "Nettoyage & Facility Management",
        "ONG & Projets Internationaux",
        "Production Industrielle",
        "Services Externalisés",
        "Technologie & IT",
        "Télécommunications",
        "Transport & Logistique",
    ])
    context = {
        "clients": clients,
        "secteurs": secteurs,

    }
    return render(request, 'site_web/espaces/espace_candidat.html', context)

def espace_consultant(request):
    clients = range(1, 16)

    secteurs = sorted([
        "Banque & Assurance",
        "BTP & Infrastructures",
        "Distribution & FMCG",
        "Grande Distribution",
        "Industrie Agroalimentaire",
        "Mines & Énergie",
        "Nettoyage & Facility Management",
        "ONG & Projets Internationaux",
        "Production Industrielle",
        "Services Externalisés",
        "Technologie & IT",
        "Télécommunications",
        "Transport & Logistique",
    ])
    context = {
        "clients": clients,
        "secteurs": secteurs,

    }


    return render(request, 'site_web/espaces/espace_consultant.html',context)


def espace_entreprise(request):

    clients = range(1, 16)

    secteurs = sorted([
        "Banque & Assurance",
        "BTP & Infrastructures",
        "Distribution & FMCG",
        "Grande Distribution",
        "Industrie Agroalimentaire",
        "Mines & Énergie",
        "Nettoyage & Facility Management",
        "ONG & Projets Internationaux",
        "Production Industrielle",
        "Services Externalisés",
        "Technologie & IT",
        "Télécommunications",
        "Transport & Logistique",
    ])

    services = [
        {
            "title": "Recrutement & Évaluation",
            "description": (
                "Identification, sélection et évaluation de profils qualifiés "
                "selon les besoins techniques et organisationnels de votre entreprise."
            ),
            "highlight": "Sélection rigoureuse",
            "icon": "users",
        },

        {
            "title": "Intérim & Mise à disposition",
            "description": (
                "Mise à disposition de personnel qualifié avec prise en charge "
                "administrative, sociale et contractuelle."
            ),
            "highlight": "Gestion RH complète",
            "icon": "briefcase",
        },

        {
            "title": "Gestion Administrative RH",
            "description": (
                "Gestion des contrats, paie, déclarations sociales et suivi "
                "administratif du personnel conformément à la réglementation malienne."
            ),
            "highlight": "Conformité sociale",
            "icon": "building",
        },

        {
            "title": "Conseil & Audit Social",
            "description": (
                "Audit RH, diagnostics organisationnels et accompagnement "
                "dans la structuration des procédures et pratiques RH."
            ),
            "highlight": "Audit & conformité",
            "icon": "shield",
        },

        {
            "title": "Formation Professionnelle",
            "description": (
                "Conception et animation de formations adaptées aux besoins "
                "opérationnels et au développement des compétences."
            ),
            "highlight": "Renforcement des capacités",
            "icon": "graduation",
        },

        {
            "title": "Sous-traitance & Appui Opérationnel",
            "description": (
                "Gestion externalisée d’activités et d’équipes opérationnelles "
                "dans les domaines logistiques, administratifs et techniques."
            ),
            "highlight": "Flexibilité opérationnelle",
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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _

def login_view(request):
   
    return render(request, 'site_web/auth/login.html')

def register_view(request):
    # Logique pour la redirection vers le formulaire d'enrôlement expert
    return render(request, 'site_web/auth/register.html')