from django.db import models
from .utils import validate_phone_namber


class Zavuch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    image = models.ImageField(upload_to='zavuch/', blank=True, null=True, verbose_name="Фото")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона", unique=True, validators=[validate_phone_namber])

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(" ", "")
        super().save(*args, **kwargs)

    def __int__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Завуч'
        verbose_name_plural = "Завучи"
