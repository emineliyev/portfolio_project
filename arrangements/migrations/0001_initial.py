# Generated by Django 4.0 on 2023-09-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mail',
            },
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='İkon adı')),
                ('icon_code', models.CharField(max_length=60, verbose_name='İkon kodu')),
            ],
            options={
                'verbose_name': 'İkonlar',
                'verbose_name_plural': 'İkonlar',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefon')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Telefon',
                'verbose_name_plural': 'Telefon',
            },
        ),
        migrations.CreateModel(
            name='SocIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Sosial şəbəkə adı')),
                ('url', models.URLField(verbose_name='Sosial şəbəkə linki')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soc_icon', to='arrangements.icons', verbose_name='İkon')),
            ],
            options={
                'verbose_name': 'İkon',
                'verbose_name_plural': 'İkonları',
            },
        ),
        migrations.CreateModel(
            name='Arrangements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Ünvan')),
                ('email', models.ManyToManyField(to='arrangements.Email', verbose_name='E-mail')),
                ('phone', models.ManyToManyField(to='arrangements.Phone', verbose_name='Telefon')),
                ('soc_icon', models.ManyToManyField(to='arrangements.SocIcon', verbose_name='Sosial şəbəkə')),
            ],
            options={
                'verbose_name': 'Ünvan',
                'verbose_name_plural': 'Ünvanı',
            },
        ),
    ]
