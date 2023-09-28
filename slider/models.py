from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Slayder adı')
    description = models.TextField(verbose_name='Slayder məzmun')
    image = models.ImageField(upload_to='slayder/%Y/%m/%d/', verbose_name='Şəkil')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayder'
