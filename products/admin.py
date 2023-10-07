from django.contrib import admin
from .models import Product, Offer, Order, Categorie
from import_export.admin import ImportExportModelAdmin


class BrandAdmin(ImportExportModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'price', 'address', 'phone', 'date', 'status')


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Product, ProductAdmin)
# Register your models here.
admin.site.register(Offer, OfferAdmin)

admin.site.register(Order, BrandAdmin)

admin.site.register(Categorie, CategorieAdmin)
