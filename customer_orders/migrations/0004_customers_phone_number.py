# Generated by Django 5.1.5 on 2025-02-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_orders', '0003_alter_customers_options_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
