from rest_framework.views import APIView
from rest_framework.response import Response
import csv, io
from .models import RegulationWater , TranslatorWater , RegulationIndustrialSoil , RegulationAgriculturalSoil, RegulationResidentialSoil, RegulationIndustrialSteam, RegulationResidentialSteam

######################################## Água ####################################################

class ImportRegulationWaterView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                RegulationWater.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    intervention_value=row['intervention_value']
                    )
        return Response({"message": "Got some data!", "data": request.data})      
    

######################################## Solo ####################################################

class ImportRegulationIndustrialSoilView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                RegulationIndustrialSoil.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    intervention_value=row['intervention_value']
                    )
        return Response({"message": "Got some data!", "data": request.data})      

class ImportRegulationAgriculturalSoilView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                RegulationAgriculturalSoil.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    intervention_value=row['intervention_value']
                    )
        return Response({"message": "Got some data!", "data": request.data})


class ImportRegulationResidentialSoilView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                RegulationResidentialSoil.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    intervention_value=row['intervention_value']
                    )
        return Response({"message": "Got some data!", "data": request.data})       


######################################## Vapor ####################################################

class ImportRegulationIndustrialSteamView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                carcinogenic=row['carcinogenic']
                noncarcinogenic=row['noncarcinogenic']
                if carcinogenic == '':
                     carcinogenic = None
                if noncarcinogenic == '':
                     noncarcinogenic = None                
                RegulationIndustrialSteam.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    carcinogenic=carcinogenic,
                    noncarcinogenic=noncarcinogenic,
                    rsl=row['rsl']
                    )
        return Response({"message": "Got some data!", "data": request.data})      


class ImportRegulationResidentialSteamView(APIView):
    def  post(self, request):       
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                carcinogenic=row['carcinogenic']
                noncarcinogenic=row['noncarcinogenic']
                if carcinogenic == '':
                     carcinogenic = None
                if noncarcinogenic == '':
                     noncarcinogenic = None     
                RegulationResidentialSteam.objects.create(
                    substance=row['substance'],
                    cas=row['cas'],
                    agency=row['agency'],
                    carcinogenic=carcinogenic,
                    noncarcinogenic=noncarcinogenic,
                    rsl=row['rsl']
                    )
        return Response({"message": "Got some data!", "data": request.data})     




######################################## Tradutor ####################################################

    
class ImportTranslatorWaterView(APIView):
    def  post(self, request):
        TranslatorWater.objects.all().delete()
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        for row in reader:
                TranslatorWater.objects.create(
                    substance_lab=row['substance_lab'],
                    cas=row['cas'],
                    substance_agency=row['substance_agency'],
                    agency=row['agency'],
                    )
        return Response({"message": "Got some data!", "data": request.data})      

