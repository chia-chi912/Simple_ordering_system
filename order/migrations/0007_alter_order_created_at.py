# Generated by Django 4.2.1 on 2023-05-30 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_order_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]