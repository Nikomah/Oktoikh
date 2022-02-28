# Generated by Django 4.0.2 on 2022-02-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oktoih', '0011_sundaytropar_voices'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvangSunday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evang', models.TextField(blank=True, verbose_name='Евангелие воскресное')),
                ('exapost', models.TextField(blank=True, verbose_name='Эксапостиларий')),
                ('st_ev', models.TextField(blank=True, verbose_name='Стихира еавнгельская')),
            ],
            options={
                'verbose_name': 'Воскресное евангелие, эксапостиларий, стихира евангельская',
                'verbose_name_plural': 'Воскресное евангелие, эксапостиларий, стихира евангельская',
            },
        ),
    ]
