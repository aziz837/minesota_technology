from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', ]
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Info, InfoAdmin)
