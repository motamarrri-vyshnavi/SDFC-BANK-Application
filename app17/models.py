from django.db import models

# Create your models here.
class account(models.Model):
    account_no=models.IntegerField()
    name=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    confirm_password=models.CharField(max_length=40)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    address=models.CharField(max_length=40)
    mobile_no=models.IntegerField()

    def __str__(self):
        return self.name
