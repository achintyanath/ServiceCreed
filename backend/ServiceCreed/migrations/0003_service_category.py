# Generated by Django 3.2.8 on 2021-11-07 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCreed', '0002_auto_20211107_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ServiceCreed.category'),
        ),
    ]