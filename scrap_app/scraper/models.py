from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Date(models.Model):
    day= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.IntegerField(validators=[MinValueValidator(datetime.date.today().year-1), MaxValueValidator(datetime.date.today().year)])
    
    
    def __str__(self):
        return self.day+'/'+self.month+'/'+self.year
