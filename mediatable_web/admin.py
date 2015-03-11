from django.contrib import admin

from mediatable_web.models import SimpleColor


class SimpleColorAdmin(admin.ModelAdmin):
    readonly_fields = ['date_of_creation']
    list_display = ['hex_color', 'date_of_creation']


admin.site.register(SimpleColor)