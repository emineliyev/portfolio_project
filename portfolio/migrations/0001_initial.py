# Generated by Django 4.0 on 2023-09-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kateqoruya')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Layihənin adı')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Layihənin slaqı')),
                ('description', models.TextField(verbose_name='Layihənin məzmunu')),
                ('client', models.CharField(max_length=255, verbose_name='Müştəri')),
                ('delivery_date', models.DateField(verbose_name='Təhvil tarixi')),
                ('portfolio_url', models.URLField(verbose_name='Layihəyə keçid')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('image', models.ImageField(upload_to='portfolio/%Y/%m/%d/', verbose_name='Şəkil')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Sayta yüklənən tarix')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category', verbose_name='Kateqoruya')),
            ],
            options={
                'verbose_name': 'Layihə',
                'verbose_name_plural': 'Layihəni',
            },
        ),
    ]