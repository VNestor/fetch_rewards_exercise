from rest_framework import serializers
from .models import Points, Transactions

# A serializer takes our models and the python code and translates into a JSON response.


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('id', 'payer', 'points')


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id', 'payer', 'points', 'timestamp')

# We create a serializer for POST requests to ensure data sent to POST request is valid.


class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('payer', 'points', 'timestamp')


class SpendPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('points',)
