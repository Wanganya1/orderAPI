from django.db import models

class Customers(models.Model):
     name = models.CharField(max_length=255)
     code = models.CharField(max_length=100,unique=True)

     def __str__(self):
        return self.name




class Order(models.Model):
    customer = models.CharField(max_length=255)
    item = models.CharField(max_length=100,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.item} ({self.customer.name})"
 







# Create your models here.
