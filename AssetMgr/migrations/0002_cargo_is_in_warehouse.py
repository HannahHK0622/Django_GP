# Generated by Django 4.1.7 on 2023-04-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMgr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='is_in_warehouse',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
