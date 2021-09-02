from django.contrib import admin
from stripe.api_resources import Customer

from .models import FitnessPlan, Customer

admin.site.register(FitnessPlan)
admin.site.register(Customer)
