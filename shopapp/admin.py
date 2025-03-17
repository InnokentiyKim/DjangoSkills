from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from shopapp.models import Product, Order
from .admin_mixins import ExportAsCSVMixin


@admin.action(description='Archive products')
def mark_as_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_as_archived, 'export_to_csv']
    list_display = ['pk', 'name', 'description_short', 'price', 'discount', 'archived']
    list_display_links = ['pk', 'name']
    ordering = ['pk', ]
    search_fields = ['name', 'description']
    fieldsets = [
        (None, {
            'fields': ['name', 'description']
        }),
        ('Price options', {
            'fields': ['price', 'discount'],
            'classes': ['collapse']
        }),
        ('Extra options', {
            'fields': ['archived'],
            'classes': ['collapse', 'wide'],
            'description': 'Extra options. Archived is for soft delete'
        })
    ]

    def description_short(self, obj: Product):
        if len(obj.description) < 40:
            return obj.description
        return obj.description[:40] + '...'


class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = ['delivery_address', 'promocode', 'created_at', 'user_verbose']

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username



