from django.db import models
from account.models import Account


class LeaderBoardEntry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    offline = models.PositiveIntegerField(default=0, verbose_name="Meters in offline")
    online_ranking = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "leaderboard entries"
