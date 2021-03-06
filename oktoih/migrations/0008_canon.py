# Generated by Django 4.0.2 on 2022-02-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oktoih', '0007_alter_sundayservicesmatins_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.IntegerField(null=True, verbose_name='Глас')),
                ('pesn1', models.TextField(blank=True, verbose_name='Песнь 1')),
                ('pesn3', models.TextField(blank=True, verbose_name='Песнь 3')),
                ('pesn4', models.TextField(blank=True, verbose_name='Песнь 4')),
                ('pesn5', models.TextField(blank=True, verbose_name='Песнь 5')),
                ('pesn6', models.TextField(blank=True, verbose_name='Песнь 6')),
                ('pesn7', models.TextField(blank=True, verbose_name='Песнь 7')),
                ('pesn8', models.TextField(blank=True, verbose_name='Песнь 8')),
                ('pesn9', models.TextField(blank=True, verbose_name='Песнь 9')),
            ],
            options={
                'verbose_name': 'Канон',
                'verbose_name_plural': 'Канон',
                'ordering': ['voice'],
            },
        ),
    ]
