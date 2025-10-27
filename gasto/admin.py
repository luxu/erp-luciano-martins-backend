from django.contrib import admin

from gasto.models import Gasto


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'datagasto',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name'
    ]
