from django.db import models

# Create your models here.
class Addpagelist(models.Model):
    titile=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.titile
    class Meta:
        ordering = ['id']