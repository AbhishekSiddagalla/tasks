# Generated by Django 5.1.4 on 2025-01-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_alter_exam_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='total',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
