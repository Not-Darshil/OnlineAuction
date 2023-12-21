from django.contrib import admin

# Register your models here.
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand','start_bid','image','date']