# Generated by Django 5.2.4 on 2025-07-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderpilot', '0005_order_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
