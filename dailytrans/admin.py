from django.contrib import admin
from .models import Daily, MasterCategory, PaymentMode, Details

# Register your models here.

admin.site.register(PaymentMode)
admin.site.register(Details)
admin.site.register(MasterCategory)
admin.site.register(Daily)