from django.shortcuts import render
from rest_framework import generics, status
from .models import Points, Transactions
from .serializers import PointsSerializer, TransactionsSerializer, AddTransactionSerializer, SpendPointsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

# Create your views here.
# This is where we will have our endpoints
# / add transactions
# / spend points
# I also want to be able to get all Points Balances, and transactions

# Returns list of Points balance from Ppoints model


class PointsView(generics.ListAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer

# Returns list of Transactions from Transactions model


class TransactionsView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

# APIView allows us to override default methods


class AddTransactionView(APIView):
    serializer_class = AddTransactionSerializer

    def post(self, request, format=None):

        # Check if data sent in POST request is valid
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Retrieve data from POST request
            payer = serializer.data.get('payer')
            points = serializer.data.get('points')
            timestamp = serializer.data.get('timestamp')
            queryset = Points.objects.filter(payer=payer)
            # if user already exists, update their points balance and create new transaction.
            if queryset.exists():
                user = queryset[0]
                user.points += points
                user.save(update_fields=['points'])
                transaction = Transactions(
                    payer=payer, points=points, timestamp=timestamp)
                transaction.save()
            # else, create new points balance for the user and create new transaction.
            else:
                user = Points(payer=payer, points=points)
                user.save()
                transaction = Transactions(
                    payer=payer, points=points, timestamp=timestamp)
                transaction.save()

            # Return 201 Created reponse when trasaction record successfully created.
            return Response(TransactionsSerializer(transaction).data, status=status.HTTP_201_CREATED)

        # Return 400 Bad Request when data passed in POST request is invalid.
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class SpendPointsView(APIView):
    serializer_class = SpendPointsSerializer

    def post(self, request, format=None):

        # Check if data sent in POST request is valid
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Retrieve data from POST request
            points = serializer.data.get('points')
            queryset = Points.objects.all()
            total_points = Points.objects.aggregate(
                Sum('points'))['points__sum']
            if total_points is not None:
                if points > total_points:
                    # Return 400 Bad Request when points passed in POST request is larger than points available.
                    return Response({'Bad Request': 'Not enough points.'}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    for user in queryset.iterator():
                        print(user.name)
                    # Return 201 Created reponse when points to spend successfully created.
                    # return Response(SpendPointsSerializer(points_to_spend).data, status=status.HTTP_201_CREATED)

            else:

                # Return 400 Bad Request when points passed in POST request is larger than points available.
                return Response({'Bad Request': 'Not enough points.'},
                                status=status.HTTP_400_BAD_REQUEST)
        # Return 400 Bad Request when data passed in POST request is invalid.
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
