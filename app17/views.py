from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.db import transaction
from app17.forms import accountForm,BalanceForm,DepositForm,WithdrawForm,TransferForm,CloseAccount
from app17.models import account as Account
from decimal import Decimal

# Create your views here.
def insertaccount(request):
    if request.method=="POST":
        form=accountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account_view")
    else:
        form=accountForm()
        return render(request,"page.html",{"form":form,'heading':'OPEN ACCOUNT FORM'})
def success(request):
    return render(request,"accountview.html")

def balance(request):
    if request.method=='POST':
        form=BalanceForm(request.POST)
        if form.is_valid():
            account_no=form.cleaned_data['account_no']
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']
            

            account=get_object_or_404(
                Account,
                account_no=account_no,
                name=name,
                password=password,
            
            )
            return render(request,'balance_result.html',{
                'account':account
            })
    else:
        form=BalanceForm()
    return render(request,'page.html',{
        'form':form,
        'heading':'BALANCE FORM'
    })
def deposit(request):
    if request.method=='POST':
        form=DepositForm(request.POST)
        account_no=request.POST.get("account_no")
        deposit_amount=Decimal(request.POST.get("deposit_amount","0"))
        account=get_object_or_404(Account,account_no=account_no)
        before_balance=account.amount
        account.amount+=deposit_amount
        account.save()
        total_balance=account.amount
        context={
            "account":account,
            "before_balance":before_balance,
            "deposit_amount":deposit_amount,
            "total_balance":total_balance,
        }
        return render(request,"deposit_result.html",context)
    else:
        form=DepositForm()
    return render(request,'page.html',{
        'form':form,
        'heading':'DEPOSIT FORM'
    
    })
def withdrawaccount(request):
   
    if request.method=='POST':
        form=WithdrawForm(request.POST)
        account_no=request.POST.get("account_no")
        withdraw_amount=Decimal(request.POST.get("withdraw_amount","0"))
        account=get_object_or_404(Account, account_no=account_no)
        before_balance=account.amount
        account.amount -= withdraw_amount
        account.save()
        total_balance= account.amount
        context={
            "account":account,
            "before_balance":before_balance,
            "withdraw_amount":withdraw_amount,
            "total_balance":total_balance,
        }
        return render(request,"withdraw_result.html",context)
    else:
        form=WithdrawForm()
    return render(request,"page.html",{
        'form':form,
        'heading':'WITHDRAW FORM'
    })
def transferaccount(request):
    if request.method=='POST':
        form=TransferForm(request.POST)
        account_no=request.POST.get("account_no")
        Target_Account_No=request.POST.get("Target_Account_No")
        amount=Decimal(request.POST.get("Transfer_amount"))
        account=get_object_or_404(Account,account_no=account_no)
        Target_Account=get_object_or_404(Account,account_no=Target_Account_No)
        if amount<=0:
            return render(request,"page.html",{"error":"Insufficient balance"})
        if account.amount < amount:
            return render(
                request,
                "page.html",
                {"error": "Insufficient balance"}
            )
        with transaction.atomic():
            account.amount-=amount
            Target_Account.amount+=amount
            account.save()
            Target_Account.save()
        return render(request,"transfer_result.html",{
            "account":Target_Account,
            'target_before_balance':Target_Account.amount-amount,
            "Transfer_amount":amount,
            "total_balance":Target_Account.amount
        })
    else:
        form=TransferForm()
    return render(request,"page.html",{
        'form':form,
        'heading':'TRANSFER FORM'
    })
def closeaccount(request):
    if request.method == "POST":
        form=CloseAccount(request.POST)

        account_no = request.POST.get('account_no')
        name = request.POST.get('name')
        password = request.POST.get('password')

        account = get_object_or_404(
            Account,
            account_no=account_no,
            name=name,
            password=password
        )

        account.delete()

        return render(
            request,
            "close_result.html",
            {
                "account_no": account_no,
                "name": name,
                "message": "Account closed successfully!"
            }
        )
    else:
        form=CloseAccount()
    return render(request,'page.html',{
        'form':form,
        'heading':'CLOSE ACCOUNT'
    })
def about(request):
    return render(request, "about.html")
def home(request):
    return render (request,"home.html")
        

