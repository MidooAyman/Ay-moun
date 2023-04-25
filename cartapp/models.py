from django.db import models

# Create your models here.

class Destination(models.Model):
   
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    ORIGINAL = 'OR'
    MIRROR = 'MI'
    EGYPTIAN = 'EG'
    CHOICES = [
        (ORIGINAL, 'Original'),
        (MIRROR, 'Mirror'),
        (EGYPTIAN, 'Egyptian'),
    ]
    des = models.CharField(max_length=2, choices=CHOICES)
    price= models.IntegerField()
    pricee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    special= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
