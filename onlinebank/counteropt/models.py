from django.db import models

# Create your models here.

class employee(models.Model):
    employee_id = models.IntegerField(primary_key = True)

class sys_manage(models.Model):
    sys_manager_id = models.IntegerField(primary_key = True)
    employee_id = models.ForeignKey(employee, on_delete = models.CASCADE)
    account = models.CharField(max_length = 100, null = False)
    password = models.CharField(max_length = 20, null = False)


class cashier(models.Model):
    cashier_id = models.IntegerField(primary_key = True)
    employee_id = models.ForeignKey(employee, on_delete = models.CASCADE)
    account = models.CharField(max_length = 100, null = False)
    password = models.CharField(max_length = 20, null = False)
    trade_authortiy = models.BooleanField(null = False)
    manage_authority = models.BooleanField(null = False)

class online_user(models.Model):
    identity_card = models.CharField(max_length = 18, null = False)

class account(models.Model):
    account_id = models.IntegerField(primary_key = True)
    password = models.IntegerField(null = False)
    identity_card = models.ForeignKey(online_user, on_delete = models.PROTECT)
    card_type = models.IntegerField(null = False)
    balance = models.FloatField(null = False)
    current_deposit = models.FloatField(null = False)
    uncredited_deposit = models.FloatField(null = False)
    is_frozen = models.BooleanField(null = False)
    is_lost = models.BooleanField(null = False)

class deposit_record(models.Model):
    deposit_record_id = models.IntegerField(primary_key = True)
    account_id = models.ForeignKey(account, on_delete = models.CASCADE)
    deposit_type = models.CharField(max_length = 10, null = False)
    auto_renew_status = models.BooleanField()
    deposit_start_date = models.DateField(null = False)
    deposit_end_date = models.DateField()
    deposit_ammount = models.FloatField(null = False)
    cashier_id = models.ForeignKey(cashier, on_delete = models.SET(0))

class withdrawal_record(models.Model):
    withdrawal_record_id = models.IntegerField(primary_key = True)
    account_id = models.ForeignKey(account, on_delete = models.CASCADE)
    withdrawal_date = models.DateField(null = False)
    withdrawal_ammount = models.FloatField(null = False)
    cashier_id = models.ForeignKey(cashier, on_delete = models.SET(0))

class transfer_record(models.Model):
    transfer_record_id = models.IntegerField(primary_key = True)
    account_in_id = models.ForeignKey(account, on_delete = models.CASCADE, related_name = 'income_transfer')
    account_out_id = models.ForeignKey(account, on_delete = models.CASCADE, related_name = 'outgo_transfer')
    transfer_date = models.DateField(null = False)
    transfer_ammount = models.FloatField(null = False)
    cashier_id = models.ForeignKey(cashier, on_delete = models.SET(0))