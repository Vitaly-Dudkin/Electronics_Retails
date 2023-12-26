from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network_management.models import Network, Supplier, Product


# Register your models here.
@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Admin panel for Network model"""

    list_display = ('name', 'email', 'phone', 'country', 'city', 'street', 'house_number', 'debt',
                    'level', 'supplier_link')
    list_filter = ('level', 'country', 'city')  # Filter by country and city
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            link = reverse('admin:network_management_supplier_change', args=[obj.supplier.pk])
            return format_html(f'<a href="{link}">{obj.supplier.name}</a>')
        return ''

    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        """Clear debt for selected networks"""

        if request.user.is_superuser:
            queryset.update(debt=0)

    clear_debt.short_description = "Clear debt"


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin panel for Supplier model"""

    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country', 'city')  # Filter by country and city
    search_fields = ('name', 'email')  # Search by name or email


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin panel for Product model"""

    list_display = ('name', 'model', 'release_date', 'price', 'network')
    list_filter = ('network', 'release_date')  # Filter by network and release date
    search_fields = ('name', 'model')  # Search by name or model
    network = ['network']
