# Generated by Django 3.2.10 on 2022-08-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]