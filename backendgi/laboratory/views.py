from rest_framework.views import APIView
from rest_framework.response import Response
import csv, io
from .translate import translate_lab_test_water, translate_lab_test_industrial_soil, translate_lab_test_agricultural_soil, translate_lab_test_residential_soil, translate_lab_test_industrial_steam, translate_lab_test_residential_steam
from .models import LabTestWater , LabTestIndustrialSoil, LabTestAgriculturalSoil, LabTestResidentialSoil, LabTestIndustrialSteam, LabTestResidentialSteam



################################################### Água ##############################################################

class ImportLabWaterView(APIView):
    def  post(self, request):
        LabTestWater.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                         if measure == "mg/L":
                              result = result*1000
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value
                    if measure == "mg/L":
                         measure = "µg/L"
                              

                    LabTestWater.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )
                    measure = row['measure']

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                                 if measure == "mg/L":
                                    result = result*1000
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value
                            if measure == "mg/L":
                                 measure = "µg/L"


                            LabTestWater.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )
                            measure = row['measure']

        translate_lab_test_water(region)                
        return Response({"message": "Got some data!", "data": request.data})


################################################# Solo ###########################################################


class ImportLabIndustrialSoilView(APIView):
    def  post(self, request):
        LabTestIndustrialSoil.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value

                    LabTestIndustrialSoil.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value


                            LabTestIndustrialSoil.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )

        translate_lab_test_industrial_soil(region)                
        return Response({"message": "Got some data!", "data": request.data})
    


class ImportLabAgriculturalSoilView(APIView):
    def  post(self, request):
        LabTestAgriculturalSoil.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value

                    LabTestAgriculturalSoil.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value


                            LabTestAgriculturalSoil.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )

        translate_lab_test_agricultural_soil(region)                
        return Response({"message": "Got some data!", "data": request.data})


class ImportLabResidentialSoilView(APIView):
    def  post(self, request):
        LabTestResidentialSoil.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value

                    LabTestResidentialSoil.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value


                            LabTestResidentialSoil.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )

        translate_lab_test_residential_soil(region)                
        return Response({"message": "Got some data!", "data": request.data})
    
################################################# Vapor ###########################################################    


class ImportLabIndustrialSteamView(APIView):
    def  post(self, request):
        LabTestIndustrialSteam.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value

                    LabTestIndustrialSteam.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value


                            LabTestIndustrialSteam.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )

        translate_lab_test_industrial_steam()                
        return Response({"message": "Got some data!", "data": request.data})
    

class ImportLabResidentialSteamView(APIView):
    def  post(self, request):
        LabTestResidentialSteam.objects.all().delete()
        region = request.data.get("region")
        report_name = request.data.get("report_name")   
        sample_type = request.data.get("sample_type") 
        data_file = request.FILES["data-file"]
        data_set = data_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string, delimiter=",")
        
        if reader.fieldnames[0] == "sample_name":
            for row in reader:
                    raw_value = row['result']
                    result = 0
                    under_limit = ""
                    measure =row['measure'] 
                    try:
                         result = float(raw_value)
                    except ValueError:
                         if '<' in raw_value:
                              under_limit = raw_value

                    LabTestResidentialSteam.objects.create(
                        report_name = report_name,
                        sample_type = sample_type,
                        substance = row['substance'],
                        sample_name = row['sample_name'],
                        result = result,
                        under_limit = under_limit,
                        measure = measure

                    )

        else:
             for row in reader:
                  substance = row['substance']
                  measure = row['measure']
                  
                  for sample_name, raw_value in row.items():
                       if sample_name != 'substance' and sample_name != 'measure':
                            result = 0
                            under_limit = ""
                            try:
                                 result = float(raw_value)
                            except ValueError:
                                 if '<' in raw_value:
                                    under_limit = raw_value


                            LabTestResidentialSteam.objects.create(
                                report_name = report_name,
                                sample_type = sample_type,    
                                substance = substance,
                                sample_name = sample_name,
                                result = result,
                                under_limit = under_limit,
                                measure = measure
                            )

        translate_lab_test_residential_steam()                
        return Response({"message": "Got some data!", "data": request.data})
