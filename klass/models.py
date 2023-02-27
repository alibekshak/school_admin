from django.db import models


class Klass(models.Model):
    letter_klass = models.CharField(max_length=1, verbose_name="Буква класса")
    number = models.PositiveIntegerField(verbose_name="Номер класса")

    @property
    def full_name(self):
        return f"{self.number} {self.letter_klass} "

    def __str__(self):
        return f"{self.number} {self.letter_klass} "

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = "Классы"
