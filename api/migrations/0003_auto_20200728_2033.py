# Generated by Django 3.0.6 on 2020-07-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200728_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_pub',
            field=models.DateField(auto_now=True),
        ),
    ]
