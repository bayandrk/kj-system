# Generated by Django 4.2.7 on 2024-06-04 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('teacher', '0030_delete_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
