
import uuid
from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=254, unique=True, blank=False, null=False)
    password = models.CharField(max_length=32)
    full_name = models.CharField(max_length=150)
    billing_address = models.CharField(max_length=250)
    default_shipping_address = models.CharField(max_length=250)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=12, null=False,
                             blank=False, unique=True)

    def __str__(self):
        return '{}'.format(self.email)

    def check_password(self, password):
        return self.password == password
