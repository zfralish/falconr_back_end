# Generated by Django 3.2.6 on 2021-08-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='trap_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
