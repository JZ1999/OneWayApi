from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    uuid = models.UUIDField(verbose_name="Unique ID", auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temporary = models.BooleanField(default=True, help_text="Is true by default and false once user registers "
                                                            "his/her email")
    last_login = models.DateTimeField()
    banned = models.BooleanField(default=False)
    device = models.CharField(max_length=255, default="UNKNOWN")

    def __str__(self):
        return f"{self.user}#{self.uuid}"
