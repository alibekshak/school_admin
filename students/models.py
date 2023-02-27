from django.db import models
from klass.models import Klass
from django.db import models


class Student(models.Model):
    name_student = models.CharField(max_length=30, verbose_name="Имя ученика")
    surname_student = models.CharField(max_length=30, verbose_name="Фамилия ученика")
    age = models.CharField(max_length=2, verbose_name="Возраст")
    image = models.ImageField(upload_to='student/', blank=True, null=True, verbose_name="Фото")
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name="Класс")

    @property
    def full_name(self):
        return f"{self.name_student} {self.surname_student} "

    def __str__(self):
        return f"{self.name_student} {self.surname_student} "

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = "Ученики"

