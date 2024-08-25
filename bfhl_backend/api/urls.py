from django.urls import path
from .views import BFHLAPIView, OperationCodeView

urlpatterns = [
    path('bfhl/', BFHLAPIView.as_view(), name='bfhl-api'),
    path('bfhl/get/', OperationCodeView.as_view(), name='operation-code-api'),
]
