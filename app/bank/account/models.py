from django.db import models

class Account(models.Model):
    account_no = models.CharField(max_length=40)
    account_email = models.EmailField(max_length=30)

    def __str__ (self):
        return(f"Acccount No: {self.account_no} test")