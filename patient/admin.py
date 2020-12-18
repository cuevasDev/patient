from django.contrib import admin
from .models import Patient, Base

# Register your models here.
admin.site.register(Base)
admin.site.register(Patient)
