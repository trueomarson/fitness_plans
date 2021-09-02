from django.contrib import admin
from stripe.api_resources import customer

from .models import FitnessPlan, Customer

admin.site.register(FitnessPlan)
admin.site.register(customer)
