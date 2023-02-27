from django.contrib import admin
from .models import Zavuch
from django.utils.safestring import mark_safe


class ZavuchAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'phone', 'get_image']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='100' height='110' >")
        return 'Нет фотографии'


admin.site.register(Zavuch, ZavuchAdmin)
