# Generated by Django 4.2 on 2025-01-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0015_alter_failedstudent_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='classroomwisesubjectwithteacher',
            old_name='teacher',
            new_name='teacher_name',
        ),
    ]
