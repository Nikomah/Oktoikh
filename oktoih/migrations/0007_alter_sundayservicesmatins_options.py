# Generated by Django 4.0.2 on 2022-02-11 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oktoih', '0006_alter_sundayservicesmatins_bg_sed1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sundayservicesmatins',
            options={'ordering': ['voice'], 'verbose_name': 'Воскресные службы утреня', 'verbose_name_plural': 'Воскресные службы утреня'},
        ),
    ]
