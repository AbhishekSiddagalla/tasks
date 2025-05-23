# Generated by Django 5.1.4 on 2025-01-08 20:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(max_length=20)),
                ('sub1', models.PositiveIntegerField(verbose_name='telugu')),
                ('sub2', models.PositiveIntegerField(verbose_name='hindi')),
                ('sub3', models.PositiveIntegerField(verbose_name='english')),
                ('sub4', models.PositiveIntegerField(verbose_name='maths')),
                ('sub5', models.PositiveIntegerField(verbose_name='science')),
                ('sub6', models.PositiveIntegerField(verbose_name='social')),
                ('total', models.PositiveIntegerField()),
                ('class_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentapp.classroom')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
