# Generated by Django 4.0.6 on 2022-09-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_mensaje_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
