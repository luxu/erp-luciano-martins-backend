from django.contrib import admin

from gasto.models import Parcelas


@admin.register(Parcelas)
class ParcelasAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'gasto',
        'parcelas',
        'numero_parcela',
        'data_parcela',
        'valor_parcela',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
        'gasto',
    ]
