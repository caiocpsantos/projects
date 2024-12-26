from . import views, export
from django.urls import path


urlpatterns = [
	path('import/water', views.ImportLabWaterView.as_view(), name='importwater'),
    path('import/industrialsoil', views.ImportLabIndustrialSoilView.as_view(), name='importindustrialsoil'),
    path('import/agriculturalsoil', views.ImportLabIndustrialSoilView.as_view(), name='importagriculturalsoil'),
    path('import/residentialsoil', views.ImportLabIndustrialSoilView.as_view(), name='importresidentialsoil'),
    path('import/industrialsteam', views.ImportLabIndustrialSoilView.as_view(), name='importresidentialsteam'),
    path('import/residentialsteam', views.ImportLabIndustrialSoilView.as_view(), name='importresidentialsteam'),
    path('export/water', export.ExportLabTestWaterXLSX.as_view(), name='exportwater'),
    path('export/industrialsoil', export.ExportLabTestIndustrialSoilXLSX.as_view(), name='exportindustrialsoil'),
    path('export/agriculturalsoil', export.ExportLabTestIndustrialSoilXLSX.as_view(), name='exportagriculturalsoil'),
    path('export/residentialsoil', export.ExportLabTestIndustrialSoilXLSX.as_view(), name='exportresidentialsoil'),
    path('export/industrialsteam', views.ImportLabIndustrialSoilView.as_view(), name='exportresidentialsteam'),
    path('export/residentialsteam', views.ImportLabIndustrialSoilView.as_view(), name='exportresidentialsteam'),
    
]