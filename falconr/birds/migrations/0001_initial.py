# Generated by Django 3.2.6 on 2021-08-16 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('trap_weight', models.FloatField()),
                ('species', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('falconer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mass', models.FloatField()),
                ('time', models.DateTimeField()),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='birds.bird')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('training_type', models.CharField(max_length=50)),
                ('performance', models.IntegerField()),
                ('notes', models.TextField()),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='birds.bird')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('game', models.CharField(max_length=25)),
                ('performance', models.IntegerField()),
                ('kills', models.IntegerField()),
                ('notes', models.TextField()),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunts', to='birds.bird')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('mass', models.FloatField()),
                ('time', models.DateTimeField()),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedings', to='birds.bird')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
