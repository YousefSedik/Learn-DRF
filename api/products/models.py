from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    
    def discount(self):
        return "%.2f" %(float(self.price)*.95) 

    def sale_price(self):
        return "%.2f" %(float(self.price)*.5)
    
    
    
