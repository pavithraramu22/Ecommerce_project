from django.db import models

# Create your models here.

class Ecommerce(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    discounted_price=models.IntegerField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=100)


class Confirmation(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    address=models.TextField()
    email=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    landmark=models.CharField(max_length=200)
