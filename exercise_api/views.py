from django.shortcuts import render
from rest_framework import generics, status
from .models import Points, Transactions
from .serializers import PointsSerializer, TransactionsSerializer, AddTransactionSerializer, SpendPointsSerializer, ToJSONSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
import datetime
from collections import defaultdict
import json
from django.http import JsonResponse

# Create your views here.
# This is where we will have our endpoints
# / add transactions
# / spend points
# I also want to be able to get all Points Balances, and transactions

# Helper function to help determine if key exist in nested dictionart
# ref: https://stackoverflow.com/a/43491315


def keys_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError(
            'keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True

# Helper function for SpendPointsView


def spend_points(points):
    sorted_transactions = Transactions.objects.all().order_by('timestamp')
    # sorted_transactions = Transactions.objects.all()
    balances = Points.objects.all()

    # Create a dictionary that will keep track of point balances during end of each day
    EOD_balances = defaultdict(dict)

    # Create a dictionary that keeps track of current point balances
    current_balances = {}

    # Iterate through transactions and retrieve necessary data.
    for transaction_idx, obj in enumerate(sorted_transactions.iterator()):
        transaction = sorted_transactions[transaction_idx]
        payer = transaction.payer
        balance = transaction.points
        temp = transaction.timestamp
        timestamp = temp.strftime('%Y-%m-%d')

        # If data found does not exist dictionary, add it
        if keys_exists(EOD_balances, timestamp, payer) == False:
            EOD_balances[timestamp][payer] = balance

        # else, update balace
        else:
            EOD_balances[timestamp][payer] += balance

        print(f"(EOD_BALANCES: {EOD_balances}")

    # Iterate through Points objects and store data to current balances
    for balance_idx, obj in enumerate(balances.iterator()):
        balance = balances[balance_idx]
        name = balance.payer
        points_at_idx = balance.points
        current_balances[name] = points_at_idx
        print(f"current balance: {current_balances}")

        # balance.save(update_fields=['points'])
        # transaction = Transactions(
        #     payer=payer, points=(points*-1), timestamp=datetime.datetime.now().replace(microsecond=0).isoformat())
        # transaction.save()
    # track_data = {"payer": [], "points": []}
    track_data = defaultdict(dict)

    # Iterate through dictionaries and determine how to spend points
    for date, users in EOD_balances.items():
        for name, current_points in current_balances.items():
            if name in EOD_balances[date] and current_points > 0 and users[name] > 0 and points > 0:
                if points - users[name] <= 0:
                    # track_data['payer'].append(name)
                    # track_data['points'].append(points)
                    track_data[name] = (points * -1)
                    points -= points
                    print(f"track data: {track_data}")
                    print(users[name])
                    print(points)
                else:
                    # track_data['payer'].append(name)
                    # track_data['points'].append(users[name])
                    track_data[name] = (users[name] * -1)
                    points -= users[name]
                    print(f"track data: {track_data}")
                    print(users[name])
                    print(points)

    to_json = json.dumps([{"payer": payer, "points": points}
                          for payer, points in track_data.items()])
    print(to_json)
    return to_json

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
            total_points = Points.objects.aggregate(
                Sum('points'))['points__sum']
            if total_points is not None:
                if points > total_points:
                    # Return 400 Bad Request when points passed in POST request is larger than points available.
                    return Response({'Bad Request': 'Not enough points.'}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    transaction = spend_points(points)

                    return JsonResponse(transaction, safe=False)
                # return Response({user.payer}, status=status.HTTP_200_OK)
                # Return 201 Created reponse when points to spend successfully created.

            else:

                # Return 400 Bad Request when points passed in POST request is larger than points available.
                return Response({'Bad Request': 'No payers found.'},
                                status=status.HTTP_400_BAD_REQUEST)
        # Return 400 Bad Request when data passed in POST request is invalid.
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
