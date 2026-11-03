from django import forms
from app17.models import account

class accountForm(forms.ModelForm):
    class Meta:
        model=account
        fields=['account_no','name','password','confirm_password','amount','address','mobile_no']
        widgets={'password':forms.PasswordInput,
                 'confirm_password':forms.PasswordInput}
class BalanceForm(forms.Form):
    account_no=forms.IntegerField()
    name=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)

class DepositForm(forms.Form):
    account_no=forms.IntegerField()
    name=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)
    deposit_amount=forms.DecimalField(max_digits=12,decimal_places=6)

class WithdrawForm(forms.Form):
    account_no=forms.IntegerField()
    name=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)
    withdraw_amount=forms.DecimalField(max_digits=12,decimal_places=6)

class TransferForm(forms.Form):
    account_no=forms.IntegerField()
    name=forms.CharField(max_length=40)

    password=forms.CharField(max_length=40)
    Target_Account_No=forms.IntegerField()
    Transfer_amount=forms.DecimalField(max_digits=12,decimal_places=6)

class CloseAccount(forms.Form):
    account_no=forms.IntegerField()
    name=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)

    
