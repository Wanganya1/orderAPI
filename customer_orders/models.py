from django.db import models
from django.utils.timezone import now

class Customers(models.Model):
     name = models.CharField(max_length=255)
     code = models.CharField(max_length=100,unique=True)
     phone_number =models.CharField(max_length=15, default='N/A')
     

     class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

     def __str__(self):
        return self.name




class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    item = models.CharField(max_length=100,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)#auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


    def __str__(self):
        return f"{self.item} ({self.customer.name})"
 







# Create your models here.
