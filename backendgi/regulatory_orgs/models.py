from django.db import models

# Create your models here.


class RegulationWater(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    intervention_value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance

######################################## Solo ####################################################


class RegulationIndustrialSoil(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    intervention_value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance

class RegulationAgriculturalSoil(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    intervention_value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance
    
class RegulationResidentialSoil(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    intervention_value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance


######################################## Vapor ####################################################


class RegulationResidentialSteam(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    carcinogenic = models.FloatField(null=True, blank=True)
    noncarcinogenic = models.FloatField(null=True, blank=True)
    rsl = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance

   
class RegulationIndustrialSteam(models.Model):
    substance = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    agency = models.CharField(max_length=30, null=False)
    carcinogenic = models.FloatField(null=True, blank=True)
    noncarcinogenic = models.FloatField(null=True, blank=True)
    rsl = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.substance    



######################################## Tradutor ####################################################



class TranslatorWater(models.Model):
    substance_lab = models.CharField(max_length=300, null=False)
    cas = models.CharField(max_length=30, null=True)
    substance_agency = models.CharField(max_length=300, null=False)
    agency = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.substance_lab


