# Generated by Django 4.2 on 2025-01-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0020_exam_sub7'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='sub7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentapp.sports'),
        ),
    ]
