# Generated by Django 2.0.2 on 2018-03-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_postagem_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='categoria',
            field=models.CharField(max_length=50, verbose_name='Categoria'),
        ),
    ]
