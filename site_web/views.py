from django.shortcuts import render

def home(request):
    return render(request, 'site_web/home/home.html')

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

from django.views.generic import DetailView

from django.views.generic import TemplateView
from django.http import Http404

class JobDetailView(TemplateView):
    template_name = 'site_web/jobs/detail_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')

        # Simulation d'une base de données Antarès
        jobs_data = {
            'assistant-rh-polyvalent': {
                'title': 'Assistant RH Polyvalent',
                'reference': 'ANT/ARHP/00270125AF',
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

                <h4>Gestion administrative du personnel :</h4>
                <ul>
                    <li>Mettre à jour les dossiers du personnel</li>
                    <li>Rédiger contrats, attestations et courriers administratifs</li>
                    <li>Gérer congés, absences et incidents</li>
                    <li>Effectuer les déclarations sociales et fiscales</li>
                    <li>Assurer le respect du règlement intérieur</li>
                </ul>

                <h4>Formation et évaluation :</h4>
                <ul>
                    <li>Identifier les besoins en formation</li>
                    <li>Organiser les sessions de formation</li>
                    <li>Mettre en place des systèmes d’évaluation</li>
                    <li>Analyser les performances et proposer des axes d’amélioration</li>
                </ul>

                <h4>Support organisationnel :</h4>
                <ul>
                    <li>Participer à l’organisation d’événements RH</li>
                    <li>Diffuser les informations internes</li>
                </ul>

                <h4>Développement commercial :</h4>
                <ul>
                    <li>Identifier de nouveaux clients</li>
                    <li>Promouvoir les services du cabinet</li>
                    <li>Fidéliser les clients existants</li>
                </ul>
                """,

                'profile_html': """
                <ul>
                    <li>Licence en Ressources Humaines, Administration ou équivalent</li>
                    <li>Minimum 2 ans d’expérience</li>
                    <li>Maîtrise du droit du travail et des outils bureautiques</li>
                    <li>Bonnes capacités rédactionnelles et relationnelles</li>
                    <li>Esprit d’équipe, rigueur et organisation</li>
                    <li>Connaissance du processus de recrutement</li>
                    <li>Maîtrise du français, anglais est un atout</li>
                    <li>Respect de la confidentialité</li>
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
            "title": "Recrutement Stratégique",
            "description": "Dénichez les talents qui feront votre croissance grâce à notre méthodologie de sourcing rigoureuse.",
            "icon": "user-group",
        },
        {
            "title": "Intérim & Mise à disposition",
            "description": "Gagnez en agilité avec du personnel qualifié immédiatement opérationnel pour vos projets critiques.",
            "icon": "clock",
        },
        {
            "title": "Externalisation RH (BPO)",
            "description": "Déléguez la complexité. Nous gérons vos processus RH pour vous permettre de vous concentrer sur votre cœur de métier.",
            "icon": "briefcase",
        },
        {
            "title": "Gestion Administrative & Paie",
            "description": "Sécurisez votre conformité sociale et optimisez la gestion de vos contrats et de votre paie au Mali.",
            "icon": "document-check",
        },
        {
            "title": "Ingénierie de Formation",
            "description": "Valorisez votre capital humain en développant les compétences clés de vos collaborateurs.",
            "icon": "academic-cap",
        },
        {
            "title": "Audit & Conseil RH",
            "description": "Identifiez vos leviers de performance et alignez votre organisation sur vos objectifs stratégiques.",
            "icon": "presentation-chart",
        },
    ]
    return render(request, 'site_web/services/services.html', {'services': services})


def savoir_plus(request):
    services_details = [
        {
            "slug": "recrutement",
            "title": "Recrutement Stratégique",
            "full_description": "Nous identifions les talents rares qui partagent vos valeurs et votre vision. Notre processus inclut le sourcing, l'évaluation psychotechnique et l'accompagnement à l'intégration.",
            "points": ["Chasse de têtes", "Évaluation de potentiel", "Recrutement de masse", "Intégration (Onboarding)"],
            "icon": "user-group"
        },
        {
            "slug": "interim",
            "title": "Intérim & Mise à disposition",
            "full_description": "Une solution flexible pour vos pics d'activité ou vos remplacements urgents. Nous gérons l'intégralité du cycle contractuel et opérationnel.",
            "points": ["Flexibilité opérationnelle", "Gestion administrative simplifiée", "Remplacement rapide", "Contrats conformes au code du travail malien"],
            "icon": "clock"
        },
        # ... Ajoutez les autres services ici avec leur propre slug
    ]
    return render(request, 'site_web/services/savoir_plus.html', {'services_details': services_details})


def espace_candidat(request):
    return render(request, 'site_web/espaces/espace_candidat.html')

