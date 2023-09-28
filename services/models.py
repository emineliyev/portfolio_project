from django.db import models

from arrangements.models import Icons


class ServiceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Xidmət adı')
    description = models.TextField(verbose_name='Xidmət haqqında')
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True, verbose_name='İkon',
                             related_name='icon_service_type')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Xidmət növü'
        verbose_name_plural = 'Xidmət növü'


class Service(models.Model):
    title = models.CharField(max_length=60, verbose_name='Xidmət başlıq')
    description = models.TextField(verbose_name='Məzmun')
    services_type = models.ManyToManyField(ServiceType, verbose_name='Xidmət növü')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmət'
