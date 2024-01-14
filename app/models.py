from django.db import models

# Create your models here.
class shop(models.Model):
    product_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.product_name
    
class products(models.Model):
    product_name = models.ForeignKey(shop, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    amount=models.BigIntegerField()
    mfg=models.DateField()
    def __str__(self):
        return self.product_name
    
