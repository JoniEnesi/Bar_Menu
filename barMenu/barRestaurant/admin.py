from django.contrib import admin
from .models import *
from django.utils.html import format_html
import json
from collections import defaultdict
from django.utils import timezone
from django.db.models import F
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ['get_table', 'order_summary', 'view_order', 'get_total_with_currency', 'is_paid']
    list_editable = ['view_order', 'is_paid']

    def get_table(self, obj):
        return f'Tavolina-{obj.table}'
    get_table.short_description = 'table'

    def get_total_with_currency(self, obj):
        return f'{obj.total} Lek'
    get_total_with_currency.short_description = 'total'


    #Kalimi i produkteve ne kolone dhe jo ne rrjeshta
    def order_summary(self, obj):
        order_items = obj.order.split('__')
        return format_html('<br>'.join(order_items))
    order_summary.short_description = 'order'

    # Krijimi kur behet is_paid i aktivitetit te diten ne modelin Overview si dhe krijimi
    # ose përditësimi përmbledhjen ditore ne modelin DailySummary
    def save_model(self, request, obj, form, change):
        if 'is_paid' in form.changed_data and obj.is_paid:

            today = timezone.now().date()
            daily_summary, created = DailySummary.objects.get_or_create(date=today)

            product_counts = defaultdict(int)
            if daily_summary.products:
                product_counts.update(daily_summary.products)

            order_items = obj.order.split('__')
            for item in order_items:
                if item.strip():
                    qty, product_name = item.split(' - ', 1)
                    product_counts[product_name] += int(qty)

            daily_summary.products = dict(product_counts)

            daily_summary.total_sales = F('total_sales') + obj.total
            daily_summary.save()

            Overview.objects.create(
                table=obj.table,
                order=obj.order,
                total=obj.total
            )

            obj.delete()
        else:
            super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
        js = ('js/admin.js',)


class OverviewAdmin(admin.ModelAdmin):
    list_display = ['get_table', 'order_summary', 'get_total_with_currency', 'paid_date']

    def get_table(self, obj):
        return f'Tavolina-{obj.table}'
    get_table.short_description = 'table'

    def get_total_with_currency(self, obj):
        return f'{obj.total} Lek'
    get_total_with_currency.short_description = 'total'


    # Kalimi i produkteve ne kolone dhe jo ne rrjeshta
    def order_summary(self, obj):
        order_items = obj.order.split('__')  #
        return format_html('<br>'.join(order_items))
    order_summary.short_description = 'order'



class DailySummaryAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin.js',)


admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Table, TableAdmin)
admin.site.register(Offer)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(DailySummary, DailySummaryAdmin)