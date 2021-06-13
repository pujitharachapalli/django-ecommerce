from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):

    def __str__(self):
        return self.name

    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.FloatField()

class Registration(models.Model):

    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,default='last-name')
    user_name = models.CharField(max_length=200,default='user-name')
    email = models.CharField(max_length=200,default='email')
    password1 = models.CharField(max_length=200,default='password')
    password2 = models.CharField(max_length=200,default='password')


