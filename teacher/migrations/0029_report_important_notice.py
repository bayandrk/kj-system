# Generated by Django 4.2.7 on 2024-05-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0028_rename_child_location_report_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Important_notice',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
