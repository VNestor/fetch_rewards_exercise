from django.urls import path
from .views import UserView, TransactionView

urlpatterns = [
    path('user', UserView.as_view()),
    path('transaction', TransactionView.as_view())
]
