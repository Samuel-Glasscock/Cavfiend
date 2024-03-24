# Generated by Django 5.0.3 on 2024-03-24 02:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaffeineIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caffeine_intake', models.IntegerField(help_text='Amount of caffeine in milligrams.')),
                ('time_of_day', models.DateTimeField(auto_now_add=True)),
                ('duration_of_consumption', models.IntegerField(help_text='Duration of consumption in days')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.IntegerField(help_text='Heart rate in beats per minute.')),
                ('sleep_hours', models.FloatField(help_text='Average hours of sleep per night.')),
                ('side_effects', models.CharField(choices=[('increased alertness', 'Increased alertness'), ('increased heart rate', 'Increased heart rate'), ('increased blood pressure', 'Increased blood pressure')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
