# Generated by Django 2.0.2 on 2018-03-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_texto_modal_modal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto_modal',
            name='modal',
            field=models.CharField(max_length=20),
        ),
    ]
