from django.contrib import admin
from .models import AdviceModel, ProductModel, ServiceModel, PartnerModel, ImagesModel, Customer_Opinion, FunctionsModel

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
    list_display = ['name', 'phone_number', 'feature_count', 'count']
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

admin.site.register([Customer_Opinion, FunctionsModel])

# <iframe width="935" height="526" src="https://www.youtube.com/embed/MnmRd6WIoIA" title="promoy sam moyka sam  сам мой сам eng arzoni eng qimmati qulayi funksiyasi kopi click bori ekanom" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>