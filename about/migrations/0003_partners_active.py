# Generated by Django 4.0 on 2023-09-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_partners_options_alter_partners_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
