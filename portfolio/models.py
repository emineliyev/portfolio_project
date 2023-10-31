from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Kateqoruya')

    def __str__(self):
        return f"{self.name}"


class Portfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name='Layihənin adı')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Layihənin slaqı')
    description = models.TextField(verbose_name='Layihənin məzmunu')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Kateqoruya')
    client = models.CharField(max_length=255, verbose_name='Müştəri')
    delivery_date = models.DateField(verbose_name='Təhvil tarixi')
    portfolio_url = models.URLField(verbose_name='Layihəyə keçid')
    status = models.BooleanField(default=True, verbose_name='Status')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Sayta yüklənən tarix')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title.replace('ə', 'e')))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[self.pk, self.slug])

    class Meta:
        verbose_name = 'Layihə'
        verbose_name_plural = 'Layihəni'


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name='Lahihə',
                                  related_name='portfolio_image')
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', verbose_name='Şəkil')
