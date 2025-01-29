# Generated by Django 5.1.5 on 2025-01-24 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ice_Cream', '0015_alter_icecreaminfo_ice_cream_flavour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IceCreamFlavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='icecreaminfo',
            name='ice_cream_flavour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ice_Cream.icecreamflavor'),
        ),
    ]
