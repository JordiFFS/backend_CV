from django.db import models

# Create your models here.
class Gender(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'({self.code}) {self.name}'
    class Meta:
        verbose_name_plural = 'Generos'


class LevelStudy(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'({self.code}) {self.name}'
    class Meta:
        verbose_name_plural = 'Niveles de estudio'

class ProfessionalTitle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = 'Títulos profesionales'

class CountryResidence(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.code}) {self.name}'
    class Meta:
        verbose_name_plural = 'Países de residencia'
