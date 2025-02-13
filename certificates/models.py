from django.db import models

# Create your models here.
class Certificates(models.Model):
    institute = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    subtitle2 = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    director = models.CharField(max_length=225)
    file = models.FileField(upload_to='certificate')
    ext = models.ForeignKey('user_ext.Ext', on_delete=models.CASCADE, related_name='certify')