from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.charfield(max_length=15,null=True,blank=True)
    lastname = models.charfield(max_length=15,null=True,blank=True)
    address = models.charfield(max_length=15,null=True,blank=True)
    age = models.charfield(max_length=15,null=True,blank=True)
    mobile = models.charfield(max_length=15,null=True,blank=True)
    cityname = models.charfield(max_length=15,null=True,blank=True)
    countryname = models.charfield(max_length=15,null=True,blank=True)
    def __str__(self) -> str:
        return self.firstname


class GetCustomerAddress(models.model):
    customer = models.Foreginkey(Customer,on_delete=models.CASCADE,null=True)
    street_name = models.Charfield(max_length=15,null=True,blank=True)
    street_number = models.Integerfield(max_length=15,null=True,blank=True)
    city = models.Charfield(max_length=15,null=True,blank=True)
    country = models.Charfield(max_length=15,null=True,blank=True)
    state = models.Charfield(max_length=15,null=True,blank=True)
    pincode = models.Integerfield(max_length=15,null=True,blank=True)
    address=models.Charfield(max_length=13,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.street_name



