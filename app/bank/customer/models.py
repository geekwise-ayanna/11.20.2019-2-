from django.db import models

class Customer(models.Model):
    customer_fname=models.CharField(max_length=30),
    customer_lname=models.CharField(max_length=30),

    def __str__ (self):
        return( f"Customer Full Name: {self.customer_fname} + {self.customer_lname}" )