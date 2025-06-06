# Generated by Django 5.1.4 on 2025-01-09 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0007_alter_exam_exam_type_delete_examtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentapp.examtype'),
        ),
    ]
