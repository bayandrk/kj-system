# Generated by Django 4.2.1 on 2024-03-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]