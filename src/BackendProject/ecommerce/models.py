from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=10, unique=True)
    price = models.IntegerField() #Price in cents
    start_date = models.CharField(max_length=10) #Date in format mm/dd/yyyy

    def __str__(self):
        return self.name