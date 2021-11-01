from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=254)
    message = models.CharField(max_length=1000)
    created_date = models.DateTimeField( auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
    
        
