from django.contrib import admin
from .models import *

class MessageAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register( ContactMessage,MessageAdmin) 

class EventsAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register( Events,EventsAdmin) 


class ProductsTypeAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register( ProductsType,ProductsTypeAdmin) 

class ProductsAdmin(admin.ModelAdmin):
    list_display=('Name',)
admin.site.register( Products,ProductsAdmin) 

class newsBlogAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register( newsBlog,newsBlogAdmin) 

