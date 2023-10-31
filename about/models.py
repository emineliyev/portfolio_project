from django.db import models
from arrangements.models import Icons


class About(models.Model):
    title = models.CharField(max_length=60, verbose_name='Başlıq')
    description = models.TextField(verbose_name='Məzmun')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'


class BusinessPlan(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlıq')
    description = models.TextField(verbose_name='Məzmun')
    image = models.ImageField(upload_to='business/%Y/%m/%d/', verbose_name='Şəkil')
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True, verbose_name='İkon',
                             related_name='icon_business_plan')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Biznes plan'
        verbose_name_plural = 'Biznes plan'


class Partners(models.Model):
    image = models.ImageField(upload_to='partners/%Y/%m/%d/', verbose_name='Şəkil')
    active = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        verbose_name = 'Tərəfdaşlar'
        verbose_name_plural = 'Tərəfdaşlar'