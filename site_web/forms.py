from django import forms

from site_web.models import Enrolement


from django import forms

from .models import Enrolement


from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Enrolement


class BaseEnrolementForm(forms.ModelForm):

    class Meta:

        model = Enrolement

        fields = [
            'nom',
            'prenom',
            'email',
            'telephone',
        ]

        widgets = {

            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Ex: Doe',

                    'class': (
                        'w-full px-5 py-3 md:px-6 md:py-4 '
                        'bg-slate-50 border border-transparent '
                        'rounded-xl md:rounded-2xl '
                        'focus:bg-white focus:ring-2 '
                        'focus:ring-blue-500 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-slate-700 text-sm md:text-base'
                    )
                }
            ),

            'prenom': forms.TextInput(
                attrs={
                    'placeholder': 'Ex: John',

                    'class': (
                        'w-full px-5 py-3 md:px-6 md:py-4 '
                        'bg-slate-50 border border-transparent '
                        'rounded-xl md:rounded-2xl '
                        'focus:bg-white focus:ring-2 '
                        'focus:ring-blue-500 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-slate-700 text-sm md:text-base'
                    )
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'john@example.com',

                    'class': (
                        'w-full px-5 py-3 md:px-6 md:py-4 '
                        'bg-slate-50 border border-transparent '
                        'rounded-xl md:rounded-2xl '
                        'focus:bg-white focus:ring-2 '
                        'focus:ring-blue-500 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-slate-700 text-sm md:text-base'
                    )
                }
            ),

            'telephone': forms.TextInput(
                attrs={
                    'placeholder': 'EX : +223 XX XX XX XX',

                    'class': (
                        'w-full px-5 py-3 md:px-6 md:py-4 '
                        'bg-slate-50 border border-transparent '
                        'rounded-xl md:rounded-2xl '
                        'focus:bg-white focus:ring-2 '
                        'focus:ring-blue-500 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-slate-700 text-sm md:text-base'
                    )
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['nom'].required = True
        self.fields['prenom'].required = True
        self.fields['email'].required = True
        self.fields['telephone'].required = True

        self.fields['nom'].error_messages = {
            'required': _(
                "Le nom est obligatoire."
            )
        }

        self.fields['prenom'].error_messages = {
            'required': _(
                "Le prénom est obligatoire."
            )
        }

        self.fields['email'].error_messages = {
            'required': _(
                "L’adresse email est obligatoire."
            ),

            'invalid': _(
                "Veuillez renseigner une adresse email valide."
            )
        }

        self.fields['telephone'].error_messages = {
            'required': _(
                "Le numéro de téléphone est obligatoire."
            )
        }

        for field_name, field in self.fields.items():

            if self.errors.get(field_name):

                field.widget.attrs['class'] += (
                    ' border border-red-400 '
                    'focus:ring-red-400 '
                )

    def clean_nom(self):

        nom = self.cleaned_data.get('nom')

        if nom:
            nom = nom.strip()

        if len(nom) < 2:

            raise ValidationError(
                _("Le nom est trop court.")
            )

        return nom

    def clean_prenom(self):

        prenom = self.cleaned_data.get('prenom')

        if prenom:
            prenom = prenom.strip()

        if len(prenom) < 2:

            raise ValidationError(
                _("Le prénom est trop court.")
            )

        return prenom

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if email:
            email = email.lower().strip()

        if Enrolement.objects.filter(email=email).exists():

            raise ValidationError(
                _(
                    "Un enrôlement existe déjà avec cette adresse email."
                )
            )

        return email

    def clean_telephone(self):

        telephone = self.cleaned_data.get('telephone')

        if telephone:
            telephone = telephone.strip()

        if len(telephone) < 8:

            raise ValidationError(
                _("Numéro de téléphone invalide.")
            )
        if Enrolement.objects.filter(telephone=telephone).exists():

            raise ValidationError(
                _(
                    "Un enrôlement existe déjà avec ce numéro de téléphone."
                )
            )


        return telephone
    
class CandidatEnrolementForm(BaseEnrolementForm):

    class Meta(BaseEnrolementForm.Meta):
        fields = BaseEnrolementForm.Meta.fields

class ConsultantEnrolementForm(BaseEnrolementForm):

    cv = forms.FileField(

        required=True,

        error_messages={
            'required': (
                "Veuillez joindre votre CV."
            )
        },

        widget=forms.ClearableFileInput(
            attrs={
                'class': (
                    'absolute inset-0 w-full h-full '
                    'opacity-0 cursor-pointer z-10'
                ),

                'accept': '.pdf,.doc,.docx'
            }
        )
    )

    class Meta(BaseEnrolementForm.Meta):

        fields = BaseEnrolementForm.Meta.fields + [
            'cv'
        ]

        widgets = {

            **BaseEnrolementForm.Meta.widgets,

            'prenom': forms.TextInput(
                attrs={
                    'placeholder': 'Moussa',

                    'class': (
                        'w-full px-0 py-2 bg-transparent '
                        'border-b-2 border-slate-100 '
                        'focus:border-emerald-500 '
                        'transition-all outline-none '
                        'text-base font-bold text-slate-900 '
                        'placeholder:text-slate-400'
                    )
                }
            ),

            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Coulibaly',

                    'class': (
                        'w-full px-0 py-2 bg-transparent '
                        'border-b-2 border-slate-100 '
                        'focus:border-emerald-500 '
                        'transition-all outline-none '
                        'text-base font-bold text-slate-900 '
                        'placeholder:text-slate-400'
                    )
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'm.coulibaly@expert.ml',

                    'class': (
                        'w-full px-0 py-2 bg-transparent '
                        'border-b-2 border-slate-100 '
                        'focus:border-emerald-500 '
                        'transition-all outline-none '
                        'text-base font-bold text-slate-900 '
                        'placeholder:text-slate-400'
                    )
                }
            ),

            'telephone': forms.TextInput(
                attrs={
                    'placeholder': 'EX: +223 XX XX XX XX',

                    'class': (
                        'w-full px-0 py-2 bg-transparent '
                        'border-b-2 border-slate-100 '
                        'focus:border-emerald-500 '
                        'transition-all outline-none '
                        'text-base font-bold text-slate-900 '
                        'placeholder:text-slate-400'
                    )
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.errors.get('cv'):

            current_class = (
                self.fields['cv']
                .widget.attrs.get('class', '')
            )

            self.fields['cv'].widget.attrs['class'] = (
                current_class + ' border-red-400'
            )

    def clean_cv(self):

        cv = self.cleaned_data.get('cv')

        if not cv:

            raise forms.ValidationError(
                "Veuillez joindre votre CV."
            )

        extensions_autorisees = [
            'pdf',
            'doc',
            'docx'
        ]

        extension = (
            cv.name
            .split('.')[-1]
            .lower()
        )

        if extension not in extensions_autorisees:

            raise forms.ValidationError(
                "Format de fichier non autorisé."
            )

        taille_max = 10 * 1024 * 1024

        if cv.size > taille_max:

            raise forms.ValidationError(
                "Le fichier dépasse la taille maximale de 10 MB."
            )

        return cv

class EntrepriseEnrolementForm(BaseEnrolementForm):

    class Meta(BaseEnrolementForm.Meta):

        fields = BaseEnrolementForm.Meta.fields + [
            'entreprise',
            'secteur_activite',
            'poste',
        ]

        widgets = {

            **BaseEnrolementForm.Meta.widgets,

            'entreprise': forms.TextInput(
                attrs={
                    'placeholder': 'Raison sociale',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'secteur_activite': forms.TextInput(
                attrs={
                    'placeholder': 'Secteur d’activité',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Nom',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'prenom': forms.TextInput(
                attrs={
                    'placeholder': 'Prénom',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'poste': forms.TextInput(
                attrs={
                    'placeholder': 'Poste occupé',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),

            'telephone': forms.TextInput(
                attrs={
                    'placeholder': 'Téléphone',

                    'class': (
                        'w-full px-6 py-5 bg-slate-100 '
                        'border border-transparent rounded-2xl '
                        'focus:ring-2 '
                        'focus:ring-antares-orange/20 '
                        'focus:border-transparent '
                        'transition-all outline-none '
                        'text-sm font-medium text-slate-700'
                    )
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['entreprise'].required = True

        self.fields['entreprise'].error_messages = {
            'required': (
                "Le nom de l’entreprise est obligatoire."
            )
        }

        for field_name, field in self.fields.items():

            if self.errors.get(field_name):

                current_class = field.widget.attrs.get(
                    'class',
                    ''
                )

                field.widget.attrs['class'] = (
                    current_class +
                    ' border border-red-400 '
                    'focus:ring-red-300 '
                )

    def clean_entreprise(self):

        entreprise = self.cleaned_data.get(
            'entreprise'
        )

        if entreprise:
            entreprise = entreprise.strip()

        if len(entreprise) < 2:

            raise forms.ValidationError(
                "Le nom de l’entreprise est trop court."
            )

        return entreprise

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if email:
            email = email.lower().strip()

        if Enrolement.objects.filter(email=email).exists():

            raise forms.ValidationError(
                (
                    "Un enrôlement existe déjà "
                    "avec cette adresse email."
                )
            )

        return email

    def clean_telephone(self):

        telephone = self.cleaned_data.get(
            'telephone'
        )

        if telephone:
            telephone = telephone.strip()

        if len(telephone) < 8:

            raise forms.ValidationError(
                "Numéro de téléphone invalide."
            )

        if Enrolement.objects.filter(
            telephone=telephone
        ).exists():

            raise forms.ValidationError(
                (
                    "Un enrôlement existe déjà "
                    "avec ce numéro de téléphone."
                )
            )

        return telephone