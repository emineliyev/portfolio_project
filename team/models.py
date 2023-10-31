from django.db import models

from arrangements.models import Icons


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ad')
    position = models.CharField(max_length=255, verbose_name='Vəzifə')
    photo = models.ImageField(upload_to='team/%Y/%m/%d/', verbose_name='Şəkil')
    soc_network_facebook = models.URLField(verbose_name='Facebook sosial şəbəkə', blank=True, null=True)
    soc_network_instagram = models.URLField(verbose_name='Instagram sosial şəbəkə', blank=True, null=True)
    soc_network_linkedin = models.URLField(verbose_name='Linkedin sosial şəbəkə', blank=True, null=True)
    soc_network_twitter = models.URLField(verbose_name='Twitter sosial şəbəkə', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
