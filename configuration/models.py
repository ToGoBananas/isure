from django.db import models
from policies.models import PolicyBase


class Currency(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    euro = models.FloatField(null=True)
    usd = models.FloatField(null=True)

    def __str__(self):
        return str(self.last_modified)

    class Meta:
        verbose_name = 'курсы валют'
        verbose_name_plural = 'Курсы валют'


class AppRules(models.Model):
    text = models.TextField()

    def __str__(self):
        return str(self.last_modified)

    class Meta:
        verbose_name = 'правила'
        verbose_name_plural = 'Правила использования приложения'


class Bordereau(models.Model):
    csv = models.FileField(upload_to='bordereau/', blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        verbose_name = 'бордеро'
        verbose_name_plural = 'Бордеро'
