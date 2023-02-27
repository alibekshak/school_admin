from django.db import models
from klass.models import Klass
from django.db import models


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=30, verbose_name="Название урока")
    time_lesson = models.CharField(max_length=5, verbose_name="Начало урока")
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name="У какого класса урок")

    @property
    def full_name(self):
        return f"{self.name_lesson}"

    def __str__(self):
        return f"{self.name_lesson}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = "Уроки"
