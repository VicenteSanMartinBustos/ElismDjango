# Generated by Django 5.0.6 on 2024-07-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elism', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='genero',
            field=models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], default='hombre', max_length=20),
        ),
    ]