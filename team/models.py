from django.db import models

from arrangements.models import Icons


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ad')
    position = models.CharField(max_length=255, verbose_name='Vəzifə')
    photo = models.ImageField(upload_to='team/%Y/%m/%d/', verbose_name='Şəkil')
    icon = models.ManyToManyField(Icons, null=True, verbose_name='İkon', related_name='icon_team')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
