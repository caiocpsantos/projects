from logging import info
from django.db import transaction
from .models import LabTestWater, LabTestIndustrialSoil, LabTestAgriculturalSoil, LabTestResidentialSoil, LabTestIndustrialSteam, LabTestResidentialSteam
from regulatory_orgs.models import TranslatorWater, RegulationWater, RegulationIndustrialSoil, RegulationResidentialSoil, RegulationAgriculturalSoil, RegulationIndustrialSteam, RegulationResidentialSteam

######################################## Água #######################################################

def translate_lab_test_water(region):

    if region == "sp":
        priorities = ["CETESB", "P888", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestWater.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationWater.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break

    if region == "br":
        priorities = ["CONAMA", "P888", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestWater.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()

                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationWater.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break


######################################## Solo #######################################################


def translate_lab_test_industrial_soil(region):

    if region == "sp":
        priorities = ["CETESB", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestIndustrialSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationIndustrialSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break

    if region == "br":
        priorities = ["CONAMA", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestIndustrialSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()

                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationIndustrialSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break      

def translate_lab_test_agricultural_soil(region):

    if region == "sp":
        priorities = ["CETESB", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestAgriculturalSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationAgriculturalSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break

    if region == "br":
        priorities = ["CONAMA", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestAgriculturalSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()

                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationAgriculturalSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break                     

          
def translate_lab_test_residential_soil(region):

    if region == "sp":
        priorities = ["CETESB", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestResidentialSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationResidentialSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break

    if region == "br":
        priorities = ["CONAMA", "EPA", "Holandesa"]

        with transaction.atomic():
            for lab_test in LabTestResidentialSoil.objects.all():
                for priority in priorities:
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance, agency = priority).first()

                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationResidentialSoil.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.intervention_value = regulatory_agency.intervention_value
                            lab_test.save()
                            break      
                    

######################################## Vapor #######################################################


def translate_lab_test_industrial_steam():

        with transaction.atomic():
            for lab_test in LabTestIndustrialSteam.objects.all():
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationIndustrialSteam.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.carcinogenic = regulatory_agency.carcinogenic
                                lab_test.noncarcinogenic = regulatory_agency.noncarcinogenic
                                lab_test.rsl = regulatory_agency.rsl
                            lab_test.save()
                            


def translate_lab_test_residential_steam():

        with transaction.atomic():
            for lab_test in LabTestResidentialSteam.objects.all():
                    translate = TranslatorWater.objects.filter(substance_lab=lab_test.substance).first()
                    if translate:
                            lab_test.substance_agency = translate.substance_agency
                            lab_test.agency = translate.agency
                            regulatory_agency = RegulationResidentialSteam.objects.filter(substance = lab_test.substance_agency, agency = lab_test.agency).first()
                            if regulatory_agency:
                                lab_test.carcinogenic = regulatory_agency.carcinogenic
                                lab_test.noncarcinogenic = regulatory_agency.noncarcinogenic
                                lab_test.rsl = regulatory_agency.rsl
                            lab_test.save()
                            

