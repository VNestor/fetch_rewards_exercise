from curses.ascii import HT
from django.shortcuts import render
from rest_framework import generics, status
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer, AddTransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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


class AddTransactionView(APIView):
    serializer_class = AddTransactionSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            payer = serializer.data.payer
            points = serializer.data.points
            timestamp = serializer.data.timestamp
            queryset = Transaction.objects.filter(id=id)
            if queryset.exists():
                transaction = queryset[0]
                transaction.payer = payer
                transaction.points = points
                transaction.timestamp = timestamp
            else:
