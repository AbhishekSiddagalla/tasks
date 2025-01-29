from django.contrib import admin
from Ice_Cream.models import IceCreamInfo



class IceCreamInfoAdmin(admin.ModelAdmin):
    list_display = ['ice_cream_flavour','ice_cream_name','ice_cream_weight','entry_date']
admin.site.register(IceCreamInfo)