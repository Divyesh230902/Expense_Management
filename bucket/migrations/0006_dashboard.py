# Generated by Django 3.2.10 on 2022-08-05 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucket', '0005_alter_basket_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('budget', models.BigIntegerField()),
                ('expanse', models.BigIntegerField(default=0)),
                ('net_amount', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
