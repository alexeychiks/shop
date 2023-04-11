from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_display_links = ('name', 'category')
    search_fields = ('category',)
    list_editable = ('price', 'available')
    list_select_related = True
    sortable_by = ('category')
    prepopulated_fields = {'url':('name',)}
    save_as = True

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':('name',)}


admin.site.register(Profile)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Characteristic)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainPictirues)
admin.site.register(Information)
admin.site.register(Contacts)