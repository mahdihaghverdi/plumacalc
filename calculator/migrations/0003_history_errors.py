# Generated by Django 3.2.16 on 2022-12-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_history_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='errors',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
