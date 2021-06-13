from django.contrib import admin
from .models import Product,Order, Registration
from django.db.models import F

# Register your models here.
admin.site.site_header = "E Commerce Website"
admin.site.site_title = "BeYoung Shopping"
admin.site.index_title = "Admin Page"


class ProductAdmin(admin.ModelAdmin):

    def change_price(self,request,queryset):
        queryset.update(discount_price = F('price')*0.9)
        # for item in queryset:
        #     item.price = item.price+10
        #     item.save()
    change_price.short_description = 'Discount Price'

    list_display = ('title','price','discount_price','category',)
    search_fields = ('title','category',)
    list_editable = ('category',)
    actions = ('change_price',)

     

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Registration)