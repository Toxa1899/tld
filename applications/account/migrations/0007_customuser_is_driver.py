# Generated by Django 5.1 on 2024-08-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customuser_address1_customuser_address2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]
