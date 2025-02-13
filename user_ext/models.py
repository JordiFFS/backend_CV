from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ext(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='ext')
    gender = models.ForeignKey("tables.Gender", on_delete=models.RESTRICT)
    levelStudy = models.ForeignKey("tables.LevelStudy", on_delete=models.RESTRICT)
    professionalTitle = models.ForeignKey("tables.ProfessionalTitle", on_delete=models.RESTRICT, null=True)
    countryResidence = models.ForeignKey("tables.CountryResidence", on_delete=models.RESTRICT)
    phone = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to='profile_pics')

class Training(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='training')
    studentTraining = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    description = models.TextField(blank=True)

class WorkExperience(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='work_experience')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    description = models.TextField(blank=True)

class Skills(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=255)
    range = models.IntegerField()
    description = models.TextField(blank=True)

    def range_srt(self):
        if (self.range < 25):
            return 'bajo'
        if (self.range >= 25 and self.range < 50):
            return 'medio-bajo'
        if (self.range >= 50 and self.range < 75):
            return 'medio-alto'
        return 'alto'

class Language(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='language')
    language = models.CharField(max_length=255)
    range = models.IntegerField()

    def range_srt(self):
        if (self.range < 25):
            return 'bajo'
        if (self.range >= 25 and self.range < 50):
            return 'medio-bajo'
        if (self.range >= 50 and self.range < 75):
            return 'medio-alto'
        return 'alto'

class Hobbys(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='hobbys')
    hobby = models.CharField(max_length=255)

class Reference(models.Model):
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='reference')
    workstation = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


