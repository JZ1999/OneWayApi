from django.contrib import admin
from account.models import Account

# Register your models here.
admin.register(Account, admin.ModelAdmin)
