# Generated by Django 5.1.4 on 2025-01-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0013_remove_exam_status_failedstudent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failedstudent',
            name='status',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
