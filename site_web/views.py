from django.shortcuts import render
from django.views.generic import DetailView

from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.shortcuts import render

from site_web.forms import (
    CandidatEnrolementForm,
    ConsultantEnrolementForm,
    EntrepriseEnrolementForm,
)

from site_web.services.contextes import (
    contexte_espaces
)

from site_web.services.contenus import (
    SERVICES_ENTREPRISE
)

from django.shortcuts import render, redirect



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
    context = {
        **contexte_espaces(),
      
    }
    return render(
        request,
        'site_web/services/services.html',
        context
    )



def espace_candidat(request):

    if request.method == 'POST':

        form = CandidatEnrolementForm(request.POST)

        if form.is_valid():

            enrolement = form.save(commit=False)

            enrolement.type_profil = 'candidat'

            enrolement.save()

            request.session['enrolement_success'] = {

                'titre': _(
                    "Votre demande a bien été reçue."
                ),

                'message': _(
                    "Nos équipes vont examiner votre "
                    "profil et procéder à la validation "
                    "de votre enrôlement."
                ),

                'details': _(
                    "Une fois votre accès approuvé, "
                    "vos identifiants de connexion "
                    "vous seront transmis par email."
                ),
            }

            return redirect('enrolement_success')

    else:
        form = CandidatEnrolementForm()

    context = {
        **contexte_espaces(),
        'form': form,
    }

    return render(
        request,
        'site_web/espaces/espace_candidat.html',
        context
    )


def espace_consultant(request):

    if request.method == 'POST':

        form = ConsultantEnrolementForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            enrolement = form.save(commit=False)

            enrolement.type_profil = 'consultant'

            enrolement.save()

            request.session['enrolement_success'] = {

                'titre': _(
                    "Votre profil consultant a bien été soumis."
                ),

                'message': _(
                    "Nos équipes procéderont à la "
                    "vérification de votre expérience "
                    "et de vos références professionnelles."
                ),

                'details': _(
                    "Après validation de votre dossier, "
                    "vos identifiants de connexion vous "
                    "seront envoyés par email."
                ),
            }

            return redirect('enrolement_success')

    else:
        form = ConsultantEnrolementForm()

    context = {
        **contexte_espaces(),
        'form': form,
    }

    return render(
        request,
        'site_web/espaces/espace_consultant.html',
        context
    )


def espace_entreprise(request):

    if request.method == 'POST':

        form = EntrepriseEnrolementForm(request.POST)

        if form.is_valid():

            enrolement = form.save(commit=False)

            enrolement.type_profil = 'entreprise'

            enrolement.save()

            request.session['enrolement_success'] = {

                'titre': _(
                    "Votre demande d’enrôlement entreprise "
                    "a bien été enregistrée."
                ),

                'message': _(
                    "Un conseiller Antarès RH prendra "
                    "prochainement contact avec votre "
                    "organisation afin de vous accompagner "
                    "dans votre onboarding."
                ),

                'details': _(
                    "Après validation de votre dossier, "
                    "vos identifiants de connexion vous "
                    "seront envoyés par email."
                ),
            }

            return redirect('enrolement_success')

    else:
        form = EntrepriseEnrolementForm()

    context = {
        **contexte_espaces(),

        'services': SERVICES_ENTREPRISE,

        'form': form,
    }

    return render(
        request,
        'site_web/espaces/espace_entreprise.html',
        context
    )


def enrolement_success(request):

    data = request.session.get(
        'enrolement_success'
    )

    if not data:
        return redirect('home')

    context = {

        'titre': data.get('titre'),

        'message': data.get('message'),

        'details': data.get('details'),
    }

    del request.session['enrolement_success']

    return render(
        request,
        'site_web/espaces/enrolement_success.html',
        context
    )



def politique_confidentialite(request):
    return render(request, 'site_web/legal/politique_confidentialite.html')

def mentions_legales(request):
    return render(request, 'site_web/legal/mentions_legales.html')

def cgu(request):
    return render(request, 'site_web/legal/cgu.html')



def login_view(request):
   
    return render(request, 'site_web/auth/login.html')

def register_view(request):
    # Logique pour la redirection vers le formulaire d'enrôlement expert
    return render(request, 'site_web/auth/register.html')