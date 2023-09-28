from django.db import models


class Testimation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ad')
    photo = models.ImageField(upload_to='testimation/%Y/%m/%d/', verbose_name='Şəkil')
    client_activate = models.CharField(max_length=255, verbose_name='Müəssisə')
    message = models.TextField(verbose_name='Mesaj')
    status = models.BooleanField(default=False, verbose_name='Status')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Şərh tarxi')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Şərh'
        verbose_name_plural = 'Şərh'
