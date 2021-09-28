from rest_framework import viewsets
from account.models import Account
from account.serializers import TemporaryAccountSerializer


class TemporaryAccountView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(temporary=True)
    serializer_class = TemporaryAccountSerializer

    def get_permissions(self):
        return [perm() for perm in self.permission_classes] if not self.request.method == "POST" else ()

    def get_authenticators(self):
        return [auth() for auth in self.authentication_classes] if not self.request.method == "POST" else ()
