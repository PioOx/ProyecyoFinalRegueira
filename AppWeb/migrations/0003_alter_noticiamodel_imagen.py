# Generated by Django 4.1.4 on 2022-12-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0002_alter_noticiamodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiamodel',
            name='Imagen',
            field=models.ImageField(upload_to='media/noticias'),
        ),
    ]
