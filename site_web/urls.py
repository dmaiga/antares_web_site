from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('jobs/', jobs, name='jobs'),
    path('jobs/<slug:slug>/', JobDetailView.as_view(), name='job_detail'),
    path('services/', services, name='services'),
    path('services/info/', savoir_plus, name='savoir_plus'),
    path('espace-candidat/', espace_candidat, name='espace_candidat'),
    path('espace-entreprise/', espace_entreprise, name='espace_entreprise'),  
    path('espace-consultant/', espace_consultant, name='espace_consultant'),
]