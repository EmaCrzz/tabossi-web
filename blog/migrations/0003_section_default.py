# Generated by Django 2.0 on 2019-04-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190404_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
