from django.urls import path
from account.views import TemporaryAccountView

urlpatterns = [
    path('temporary', TemporaryAccountView.as_view({"post": "create"})),
    path('temporary/<uuid:uuid>', TemporaryAccountView.as_view({"get": "retrieve"})),
]
