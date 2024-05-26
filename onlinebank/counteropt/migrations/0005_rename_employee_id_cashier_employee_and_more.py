# Generated by Django 5.0.6 on 2024-05-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counteropt', '0004_rename_trade_authortiy_cashier_trade_authority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashier',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='sys_manage',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.AlterField(
            model_name='deposit_record',
            name='cashier_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transfer_record',
            name='cashier_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='withdrawal_record',
            name='cashier_id',
            field=models.IntegerField(),
        ),
    ]
