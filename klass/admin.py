from django.contrib import admin
from .models import Klass
from django.utils.safestring import mark_safe


class KlassAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'number']


admin.site.register(Klass, KlassAdmin)