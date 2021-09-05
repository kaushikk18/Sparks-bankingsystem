from sparks_bank.views import review
from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models

from .models import customer, transaction_record, Review


class customeradmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("cust_name",)}

# Register your models here.


admin.site.register(customer)
admin.site.register(transaction_record)
admin.site.register(Review)
