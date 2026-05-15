from .contenus import CLIENTS, SECTEURS, SERVICES_ENTREPRISE, PAGE_SERVICE


def contexte_espaces():

    return {
        "clients": CLIENTS,
        "secteurs": SECTEURS,
        "services_entreprise": SERVICES_ENTREPRISE,
        "page_service": PAGE_SERVICE,
    }