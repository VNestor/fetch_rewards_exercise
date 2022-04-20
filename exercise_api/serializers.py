from rest_framework import serializers
from .models import User, Transaction

# A serializer takes our models and the python code and translates into a JSON response.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'points')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'payer', 'points', 'timestamp')
