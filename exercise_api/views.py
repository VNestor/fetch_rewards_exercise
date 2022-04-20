from curses.ascii import HT
from django.shortcuts import render
from rest_framework import generics
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer

# Create your views here.
# This is where we will have our endpoints
# / add transaction
# / spend points
# I also want to be able to get all users, and a transactions


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
