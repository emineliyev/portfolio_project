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
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('position', models.CharField(max_length=255, verbose_name='Vəzifə')),
                ('photo', models.ImageField(upload_to='team/%Y/%m/%d/', verbose_name='Şəkil')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='SocIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Sosial şəbəkə adı')),
                ('url', models.URLField(verbose_name='Sosial şəbəkə linki')),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icon_team', to='arrangements.icons', verbose_name='İkon')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icon', to='team.team', verbose_name='Əlaqə')),
            ],
            options={
                'verbose_name': 'İkon',
                'verbose_name_plural': 'İkonları',
            },
        ),
    ]
