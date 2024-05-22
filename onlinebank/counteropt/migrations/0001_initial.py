# Generated by Django 5.0.6 on 2024-05-22 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.IntegerField()),
                ('card_type', models.IntegerField()),
                ('balance', models.FloatField()),
                ('current_deposit', models.FloatField()),
                ('uncredited_deposit', models.FloatField()),
                ('is_frozen', models.BooleanField()),
                ('is_lost', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='cashier',
            fields=[
                ('cashier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('trade_authortiy', models.BooleanField()),
                ('manage_authority', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='online_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_card', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='deposit_record',
            fields=[
                ('deposit_record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('deposit_type', models.CharField(max_length=10)),
                ('auto_renew_status', models.BooleanField()),
                ('deposit_start_date', models.DateField()),
                ('deposit_end_date', models.DateField()),
                ('deposit_ammount', models.FloatField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counteropt.account')),
                ('cashier_id', models.ForeignKey(on_delete=models.SET(0), to='counteropt.cashier')),
            ],
        ),
        migrations.AddField(
            model_name='cashier',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counteropt.employee'),
        ),
        migrations.AddField(
            model_name='account',
            name='identity_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='counteropt.online_user'),
        ),
        migrations.CreateModel(
            name='sys_manage',
            fields=[
                ('sys_manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counteropt.employee')),
            ],
        ),
        migrations.CreateModel(
            name='transfer_record',
            fields=[
                ('transfer_record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('transfer_date', models.DateField()),
                ('transfer_ammount', models.FloatField()),
                ('account_in_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_transfer', to='counteropt.account')),
                ('account_out_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgo_transfer', to='counteropt.account')),
                ('cashier_id', models.ForeignKey(on_delete=models.SET(0), to='counteropt.cashier')),
            ],
        ),
        migrations.CreateModel(
            name='withdrawal_record',
            fields=[
                ('withdrawal_record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('withdrawal_date', models.DateField()),
                ('withdrawal_ammount', models.FloatField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counteropt.account')),
                ('cashier_id', models.ForeignKey(on_delete=models.SET(0), to='counteropt.cashier')),
            ],
        ),
    ]
