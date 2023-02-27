from django.db import models

from django.db import models
from .utils import validate_phone_namber
from klass.models import Klass


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя учителя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия учителя")
    image = models.ImageField(upload_to='teacher/', blank=True, null=True, verbose_name="Фото")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона", unique=True, validators=[validate_phone_namber])
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name="Класс учителя")

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(" ", "")
        super().save(*args, **kwargs)

    def __int__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = "Учителя"
