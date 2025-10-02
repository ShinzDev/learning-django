from django.db import models

# Create your models here.


# databases models

class Api(models.Model):
    title = models.CharField(max_length=200)
    Images=models.ImageField(max_length=255)
    description = models.TextField()
    
    