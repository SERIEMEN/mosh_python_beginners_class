from django.contrib import admin
from .models import Product, Offer

# admin.site.register(Product)
# telling us that we want to manage our code/ products in the admin area
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
# the structure is the name of moedel then add the surfex model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Offer,OfferAdmin)
admin.site.register(Product, ProductAdmin)

# the productAdmin will show to present the product not just product(1) but the name it self like orange

# Register your models here.
