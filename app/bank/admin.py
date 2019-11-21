# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from bank.account.models import Account
from bank.customer.models import Customer
from bank.product.models import Product

# Register your models here.
admin.site.register(Account)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.site_header = 'Welcome to Geekwise Bank'
