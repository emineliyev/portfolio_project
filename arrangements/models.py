from django.db import models


class Icons(models.Model):
    name = models.CharField(max_length=60, verbose_name='İkon adı')
    icon_code = models.CharField(max_length=60, verbose_name='İkon kodu')

    def __str__(self):
        return f"{self.icon_code} {self.icon_code}"

    class Meta:
        verbose_name = 'İkonlar'
        verbose_name_plural = 'İkonlar'


class Phone(models.Model):
    phone = models.PositiveIntegerField(verbose_name='Telefon')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return f"{self.phone}"

    class Meta:
        verbose_name = 'Telefon'
        verbose_name_plural = 'Telefon'


class Email(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mail'


class SocIcon(models.Model):
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True, verbose_name='İkon', related_name='soc_icon')
    name = models.CharField(max_length=60, verbose_name='Sosial şəbəkə adı')
    url = models.URLField(verbose_name='Sosial şəbəkə linki')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return f"{self.icon}"

    class Meta:
        verbose_name = 'İkon'
        verbose_name_plural = 'İkonları'


class Arrangements(models.Model):
    address = models.CharField(max_length=255, verbose_name='Ünvan')
    phone = models.ManyToManyField(Phone, verbose_name='Telefon')
    email = models.ManyToManyField(Email, verbose_name='E-mail')
    soc_icon = models.ManyToManyField(SocIcon, verbose_name='Sosial şəbəkə')

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = 'Ünvan'
        verbose_name_plural = 'Ünvanı'
