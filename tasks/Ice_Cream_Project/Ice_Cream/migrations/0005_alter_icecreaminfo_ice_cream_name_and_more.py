# Generated by Django 5.1.5 on 2025-01-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ice_Cream', '0004_alter_icecreaminfo_registered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreaminfo',
            name='ice_cream_name',
            field=models.CharField(choices=[('MCH', 'Madagascar choco'), ('FVN', 'French Vanilla'), ('SBF', 'Strawberry fudge'), ('CRD', 'caramel dip'), ('FOR', 'Fresh Orange')], default=None, max_length=30, null=True),
        ),
        migrations.RemoveField(
            model_name='icecreaminfo',
            name='ice_cream_type',
        ),
        migrations.AddField(
            model_name='icecreaminfo',
            name='ice_cream_flavour',
            field=models.CharField(choices=[('SB', 'Strawberry'), ('VN', 'Vanilla'), ('CH', 'Chocolate'), ('CR', 'Caramel'), ('OR', 'Orange')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='icecreaminfo',
            name='ice_cream_weight',
            field=models.CharField(choices=[('100gms', '100'), ('250gms', '250'), ('500gms', '500')], default=None, max_length=6, null=True, verbose_name='weight in Grams'),
        ),
        migrations.DeleteModel(
            name='IceCreamName',
        ),
        migrations.DeleteModel(
            name='IceCreamType',
        ),
    ]
