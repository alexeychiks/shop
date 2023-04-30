from django.contrib import admin

from .models import (Category, Characteristic, MainPictures, Product,
                     ProductSize, Profile, Size)


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_display_links = ('name', 'category')
    search_fields = ('category',)
    list_editable = ('price', 'available')
    list_select_related = True
    inlines = (ProductSizeInline,)
    sortable_by = ('category')
    prepopulated_fields = {'url': ('name',)}
    save_as = True


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


admin.site.register(Profile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Characteristic)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(MainPictures)
