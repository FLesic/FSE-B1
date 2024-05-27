# Generated by Django 5.0.6 on 2024-05-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counteropt', '0002_employee_employee_name_employee_employee_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cashier',
            name='cashier_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deposit_record',
            name='deposit_record_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sys_manage',
            name='sys_manager_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transfer_record',
            name='transfer_record_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='withdrawal_record',
            name='withdrawal_record_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]