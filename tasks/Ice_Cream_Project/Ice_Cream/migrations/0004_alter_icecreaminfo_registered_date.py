# Generated by Django 5.1.5 on 2025-01-23 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ice_Cream', '0003_rename_registered_date_icecreaminfo_registered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreaminfo',
            name='registered_date',
            field=models.DateField(),
        ),
    ]
