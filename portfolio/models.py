from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Kateqoruya')


class Portfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name='Layihənin adı')
    slug = models.SlugField(max_length=255, verbose_name='Layihənin slaqı')
    description = models.TextField(verbose_name='Layihənin məzmunu')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kateqoruya')
    client = models.CharField(max_length=255, verbose_name='Müştəri')
    delivery_date = models.DateField(verbose_name='Təhvil tarixi')
    portfolio_url = models.URLField(verbose_name='Layihəyə keçid')
    status = models.BooleanField(default=False, verbose_name='Status')
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/', verbose_name='Şəkil')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Sayta yüklənən tarix')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[self.pk, self.slug])

    class Meta:
        verbose_name = 'Layihə'
        verbose_name_plural = 'Layihəni'
