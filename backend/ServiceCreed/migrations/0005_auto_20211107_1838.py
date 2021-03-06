# Generated by Django 3.2.8 on 2021-11-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCreed', '0004_auto_20211107_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='isSubscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='subscriptionPeriod',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=16, null=True),
        ),
    ]
