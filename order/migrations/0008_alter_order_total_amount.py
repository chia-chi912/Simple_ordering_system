# Generated by Django 4.2.1 on 2023-05-30 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0007_alter_order_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_amount",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]