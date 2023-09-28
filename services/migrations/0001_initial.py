# Generated by Django 4.0 on 2023-09-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arrangements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Xidmət adı')),
                ('description', models.TextField(verbose_name='Xidmət haqqında')),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icon_service_type', to='arrangements.icons', verbose_name='İkon')),
            ],
            options={
                'verbose_name': 'Xidmət növü',
                'verbose_name_plural': 'Xidmət növü',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Xidmət başlıq')),
                ('description', models.TextField(verbose_name='Məzmun')),
                ('services_type', models.ManyToManyField(to='services.ServiceType', verbose_name='Xidmət növü')),
            ],
            options={
                'verbose_name': 'Xidmət',
                'verbose_name_plural': 'Xidmət',
            },
        ),
    ]