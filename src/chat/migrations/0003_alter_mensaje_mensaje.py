# Generated by Django 4.0.6 on 2022-09-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_mensaje_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=models.CharField(max_length=100),
        ),
    ]