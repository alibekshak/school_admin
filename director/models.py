from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя директор")
    surname = models.CharField(max_length=100, verbose_name="Фамилия директора")
    phone = models.CharField(max_length=12,  unique=True, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='director_photo/', blank=True, null=True, verbose_name='Фото')

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(" ", "")
        super().save(*args, **kwargs)

    def __int__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = "Директора"
