# Generated by Django 3.1.5 on 2021-01-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_preferences_users', '0002_auto_20200821_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferencemodel',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelTable(
            name='userpreferencemodel',
            table='user_preferences',
        ),
    ]
