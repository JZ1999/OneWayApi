from django.contrib import admin
from game.models import LeaderBoardEntry

# Register your models here.
admin.site.register(LeaderBoardEntry, admin.ModelAdmin)
