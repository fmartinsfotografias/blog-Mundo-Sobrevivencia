# Generated by Django 4.0.4 on 2022-04-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_alter_materia_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='resumo',
            field=models.CharField(max_length=400),
        ),
    ]
