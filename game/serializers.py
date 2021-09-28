from django.shortcuts import get_object_or_404
from rest_framework import serializers

from account.models import Account
from game.models import LeaderBoardEntry


class LeaderBoardsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="account.user.first_name")
    distance = serializers.IntegerField(source="offline")
    account_uuid = serializers.UUIDField(source="account.uuid")

    class Meta:
        model = LeaderBoardEntry
        fields = ("name", "distance", "account_uuid")

    def create(self, validated_data):
        account, name, distance = validated_data.get("account").get("uuid"),\
                                  validated_data.get("account").get("user").get("first_name"),\
                                  validated_data.get("offline")
        return LeaderBoardEntry.objects.create(account=get_object_or_404(Account, uuid=account), offline=distance)
