from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

from shopapp.models import Product, Order, ProductImage
from .admin_mixins import ExportAsCSVMixin
from .forms import CSVImportForm


@admin.action(description='Archive products')
def mark_as_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    change_list_template = 'shopapp/products_changelist.html'
    actions = [mark_as_archived, 'export_to_csv']
    list_display = ['pk', 'name', 'description_short', 'price', 'discount', 'archived']
    list_display_links = ['pk', 'name']
    ordering = ['pk', ]
    search_fields = ['name', 'description']
    inlines = [ProductImageInline, ]
    fieldsets = [
        (None, {
            'fields': ['name', 'description']
        }),
        ('Price options', {
            'fields': ['price', 'discount'],
            'classes': ['collapse']
        }),
        ('Images', {
            'fields': ['preview', ],
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

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        form = CSVImportForm()
        context = {
            'form': form,
        }
        return render(request, 'admin/csv_form.html', context=context)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "import-products-csv/",
                self.import_csv,
                name="import_products_csv"
            )
        ]
        return new_urls + urls


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



