# Generated by Django 3.2.16 on 2022-12-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_history_errors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='answer',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
