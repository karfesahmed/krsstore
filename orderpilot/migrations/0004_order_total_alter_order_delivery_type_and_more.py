# Generated by Django 5.2.4 on 2025-07-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderpilot', '0003_alter_order_idwilaya'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
