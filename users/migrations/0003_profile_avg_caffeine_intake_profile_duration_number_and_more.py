# Generated by Django 5.0.3 on 2024-03-24 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avg_caffeine_intake',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='duration_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='duration_type',
            field=models.CharField(choices=[('days', 'Days'), ('weeks', 'Weeks')], default='days', max_length=5),
        ),
    ]
