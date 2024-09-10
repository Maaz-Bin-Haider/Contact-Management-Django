from django.db import models

# Create your models here.
class Add_Contact(models.Model):
    name  = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone  = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name