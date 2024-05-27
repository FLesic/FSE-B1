# Generated by Django 5.0.6 on 2024-05-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counteropt', '0005_rename_employee_id_cashier_employee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit_record',
            old_name='deposit_ammount',
            new_name='deposit_amount',
        ),
        migrations.RenameField(
            model_name='transfer_record',
            old_name='transfer_ammount',
            new_name='transfer_amount',
        ),
        migrations.RenameField(
            model_name='withdrawal_record',
            old_name='withdrawal_ammount',
            new_name='withdrawal_amount',
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='account',
            name='current_deposit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_frozen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_lost',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='uncredited_deposit',
            field=models.FloatField(default=0.0),
        ),
    ]
