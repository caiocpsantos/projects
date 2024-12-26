from django.db import models


################################## Água ############################################

class LabTestWater(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    intervention_value = models.FloatField(null=True, blank=True)


    def __str__(self):
       return self.report_name

################################## Solo ############################################

class LabTestIndustrialSoil(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    intervention_value = models.FloatField(null=True, blank=True)


    def __str__(self):
       return self.report_name


class LabTestAgriculturalSoil(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    intervention_value = models.FloatField(null=True, blank=True)


    def __str__(self):
       return self.report_name
    
    
class LabTestResidentialSoil(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    intervention_value = models.FloatField(null=True, blank=True)


    def __str__(self):
       return self.report_name    

################################## Vapor ############################################       

class LabTestIndustrialSteam(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    carcinogenic = models.FloatField(null=True, blank=True)
    noncarcinogenic = models.FloatField(null=True, blank=True)
    rsl = models.FloatField(null=False, blank=False)



    def __str__(self):
       return self.report_name



class LabTestResidentialSteam(models.Model):
    report_name = models.CharField(max_length=30, null=False)
    sample_type = models.CharField(max_length=30, null=False)
    sample_name = models.CharField(max_length=300, null=False)
    substance = models.CharField(max_length=300, null=False)
    substance_agency = models.CharField(max_length=300, null=True, blank= True)
    agency = models.CharField(max_length=30, null=True, blank=True)
    result = models.FloatField(null=False)
    under_limit = models.CharField(max_length=300, null=True, blank=True)
    measure = models.CharField(max_length=30, null=True, blank=True)
    carcinogenic = models.FloatField(null=True, blank=True)
    noncarcinogenic = models.FloatField(null=True, blank=True)
    rsl = models.FloatField(null=False, blank=False)


    def __str__(self):
       return self.report_name    
