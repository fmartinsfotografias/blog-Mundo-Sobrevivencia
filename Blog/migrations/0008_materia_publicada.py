# Generated by Django 4.0.4 on 2022-04-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_materia_resumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
