import datetime

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from account.models import Account
from game.models import LeaderBoardEntry


class TemporaryAccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.first_name")

    class Meta:
        model = Account
        fields = ("name", "uuid", "device")

    def create(self, validated_data):
        uuid, name, device = str(validated_data.get("uuid")), validated_data.get("user").get("first_name") \
            , validated_data.get("device")
        user = User.objects.filter(username=uuid).first()
        if not user:
            user = User.objects.create_user(username=uuid,
                                            password=uuid)
            user.first_name = name
            user.save()
            account = Account.objects.create(uuid=uuid, user=user, temporary=True,
                                             last_login=datetime.datetime.now(), device=device)
            LeaderBoardEntry.objects.create(account=account)
            return account
        return get_object_or_404(Account, user=user)
