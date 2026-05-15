from django.utils.translation import gettext_lazy as _


CLIENTS = range(1, 16)


SECTEURS = sorted([
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


SERVICES_ENTREPRISE = [

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
                "administratif du personnel conformément à la réglementation Malienne."
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

PAGE_SERVICE = [
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
            "description": _("Gestion des contrats, paie, déclarations sociales et suivi administratif du personnel conformément à la réglementation Malienne."),
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
