from django.contrib import admin
from .models import business_profile, Product


class BusinessProfileAdmin(admin.ModelAdmin):
        list_display=('business_name', 'business_email', 'business_num', 'business_category', 'opening_time', 'closing_time')
        search_fields=('business_name','business_category')
# Register your models here.
admin.site.register(business_profile,BusinessProfileAdmin)
admin.site.register(Product)