from . import views
from django.urls import path


urlpatterns = [
	path('water', views.ImportRegulationWaterView.as_view(), name='water'),
    path('industrialsoil', views.ImportRegulationIndustrialSoilView.as_view(), name='industrialsoil'),
    path('agriculturalsoil', views.ImportRegulationAgriculturalSoilView.as_view(), name='agriculturalsoil'),
    path('residentialsoil', views.ImportRegulationResidentialSoilView.as_view(), name='residentialsoil'),
    path('industrialsteam', views.ImportRegulationIndustrialSteamView.as_view(), name='industrialsteam'),
    path('residentialsteam', views.ImportRegulationResidentialSteamView.as_view(), name='residentialsteam'),
    path('translatorwater', views.ImportTranslatorWaterView.as_view(), name='translatorwater')
]