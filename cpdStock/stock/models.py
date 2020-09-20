from django.db import models

class Stuff(models.Model):
    tittle = models.CharField(max_length=100,blank=True,default="")
    description = models.CharField(max_length=1000,blank=True,default="")
    position_X = models.IntegerField(default=0,blank=True)
    position_Y = models.IntegerField(default=0,blank=True)
    position_Z = models.IntegerField(default=0,blank=True)
    quantity = models.IntegerField(default=0,blank=True)
    
    def __str__(self):
        return self.tittle
# Create your models here.
