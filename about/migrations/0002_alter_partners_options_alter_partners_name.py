# Generated by Django 4.0 on 2023-09-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Müştərilər', 'verbose_name_plural': 'Müştərilər'},
        ),
        migrations.AlterField(
            model_name='partners',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Müştəri adı'),
        ),
    ]