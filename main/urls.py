from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mitglied-werden/', views.mitgliedwerden, name="mitgliedwerden"),
    path('preise/', views.preise, name="preise"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('kontakt-erfolgreich/', views.kontakterfolgreich, name="kontakterfolgreich"),
    path('impressum/', views.impressum, name="impressum"),
    path('datenschutz/', views.datenschutz, name="datenschutz"),
]
