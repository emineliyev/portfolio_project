from django.db import models

from arrangements.models import Icons


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ad')
    position = models.CharField(max_length=255, verbose_name='Vəzifə')
    photo = models.ImageField(upload_to='team/%Y/%m/%d/', verbose_name='Şəkil')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'


class SocIcon(models.Model):
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True, verbose_name='İkon', related_name='icon_team')
    name = models.CharField(max_length=60, verbose_name='Sosial şəbəkə adı')
    url = models.URLField(verbose_name='Sosial şəbəkə linki')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Əlaqə', related_name='icon')

    def __str__(self):
        return f"{self.icon}"

    class Meta:
        verbose_name = 'İkon'
        verbose_name_plural = 'İkonları'
