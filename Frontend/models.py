from django.db import models

# Create your models here.
class contactdb(models.Model):
    contactname = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    contactnumber = models.IntegerField(null=True,blank=True)
    subject = models.CharField(max_length=50,null=True,blank=True)
    suggestion = models.CharField(max_length=150,null=True,blank=True)

class signupdb(models.Model):
    fullname = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    productname = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)


class bookingdb(models.Model):
    fullname = models.CharField(max_length=50,blank=True,null=True)
    username = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    productname = models.CharField(max_length=50,blank=True,null=True)
    totalprice = models.IntegerField(blank=True,null=True)

