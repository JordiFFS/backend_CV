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