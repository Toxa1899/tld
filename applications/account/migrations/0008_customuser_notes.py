# Generated by Django 5.1.1 on 2024-09-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customuser_is_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notes',
            field=models.TextField(default=1, verbose_name='Notes'),
            preserve_default=False,
        ),
    ]
