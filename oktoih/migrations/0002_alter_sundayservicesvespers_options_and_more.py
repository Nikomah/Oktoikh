# Generated by Django 4.0 on 2022-01-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oktoih', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sundayservicesvespers',
            options={'ordering': ['voice'], 'verbose_name': 'Воскресные службы вечерня', 'verbose_name_plural': 'Воскресные службы вечерня'},
        ),
        migrations.AlterField(
            model_name='sundayservicesvespers',
            name='voice',
            field=models.CharField(max_length=40),
        ),
    ]
