from django.urls import path
from .views import PointsView, TransactionsView, AddTransactionView, SpendPointsView

urlpatterns = [
    path('points', PointsView.as_view()),
    path('transactions', TransactionsView.as_view()),
    path('add-transaction', AddTransactionView.as_view()),
    path('spend-points', SpendPointsView.as_view())
]
