from django.contrib import admin
from django.db.models import F

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'created_at', 'name_category')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = 'name_category',
    readonly_fields = ('id', 'created_at')
    save_on_top = True

    actions = ['change_price']

    def change_price(self, request, queryset):
        queryset.update(price=F('price') + 100.0)

    change_price.short_description = 'Увеличить цену на 100'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'description')
    list_display_links = ('id', 'name_category')
    search_fields = 'name_category',


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
