from django.contrib import admin
from .models import Lesson
from django.utils.safestring import mark_safe


class LessonAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'klass', "time_lesson"]


admin.site.register(Lesson, LessonAdmin)
