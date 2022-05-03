from django.contrib import admin
from .models import Regime, Dictateur,Election

# Register your models here.
admin.site.register(Regime)
admin.site.register(Dictateur)
# admin.site.register(Paysan)
admin.site.register(Election)
