from django.contrib import admin
from .models import AdviceModel, ProductModel, ServiceModel, PartnerModel, ImagesModel

admin.site.register(ImagesModel)
@admin.register(ServiceModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'currency', 'create_time', 'important']
    list_editable = ['important']
    list_filter = ['create_time']
    date_hierarchy = 'create_time'
    search_fields = ['title']
    ordering = ["-create_time"]


@admin.register(PartnerModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'create_time', 'important']
    list_editable = ['important']
    list_filter = ['create_time']
    date_hierarchy = 'create_time'
    search_fields = ['name']
    ordering = ["-create_time"]


@admin.register(ProductModel)
class LeedsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'product', 'count']
    list_filter = ['create_time']
    date_hierarchy = 'create_time'
    search_fields = ['name', 'phone_number']
    ordering = ["-create_time"]

@admin.register(AdviceModel)
class LeedsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'address', 'create_time']
    list_filter = ['create_time']
    date_hierarchy = 'create_time'
    search_fields = ['name', 'phone_number']
    ordering = ["-create_time"]