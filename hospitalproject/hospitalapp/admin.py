from django.contrib import admin

# Register your models here.
from . models import Doctor
from .models import Medicine
admin.site.register(Doctor)
admin.site.register(Medicine)