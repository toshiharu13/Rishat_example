from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(
        'Цена в рублях',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)],)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
