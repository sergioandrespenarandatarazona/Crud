from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class reflexion(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    portada=models.ImageField()
    audio=models.CharField(max_length=320)



