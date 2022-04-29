from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Points, Transactions
import json

# Create your tests here.
# ref: https://www.django-rest-framework.org/api-guide/testing/


class AddTransactionTest(APITestCase):
    def test_add_transaction(self):
        """
            Ensure we can add transactions
        """
        add_transaction_url = '/add-transaction'
        data = {"payer": "DANNON", "points": 1000,
                "timestamp": "2020-11-02T14:00:00Z"}
        add_transaction_response = self.client.post(
            add_transaction_url, data, format='json')
        self.assertEqual(add_transaction_response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Transactions.objects.count(), 1)


class PointsTest(APITestCase):

    def test_points_route(self):
        """
        Ensure we can call Points route
        """
        add_transaction_url = '/add-transaction'
        data = {"payer": "DANNON", "points": 1000,
                "timestamp": "2020-11-02T14:00:00Z"}
        add_transaction_response = self.client.post(
            add_transaction_url, data, format='json')
        points_url = '/points'
        response = self.client.get(points_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Transactions.objects.count(), 1)
        self.assertEqual(json.loads(response.content), ([{
            "id": 1,
            "payer": "DANNON",
            "points": 1000
        }]
        ))


class TransactionsTest(APITestCase):

    def test_points_route(self):
        """
        Ensure we can call Points route
        """
        add_transaction_url = '/add-transaction'
        data = {"payer": "DANNON", "points": 1000,
                "timestamp": "2020-11-02T14:00:00Z"}
        add_transaction_response = self.client.post(
            add_transaction_url, data, format='json')
        points_url = '/transactions'
        response = self.client.get(points_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Transactions.objects.count(), 1)
        self.assertEqual(json.loads(response.content), ([{
            "id": 1,
            "payer": "DANNON",
            "points": 1000,
            "timestamp": "2020-11-02T14:00:00Z"
        }]
        ))


class SpendPointsTest(APITestCase):

    def test_points_route(self):
        """
        Ensure we can call Points route
        """
        add_transaction_url = '/add-transaction'
        data = {"payer": "DANNON", "points": 1000,
                "timestamp": "2020-11-02T14:00:00Z"}
        add_transaction_response = self.client.post(
            add_transaction_url, data, format='json')
        spend_points_url = '/spend-points'
        points_data = {"points": 100}
        response = self.client.post(
            spend_points_url, points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Transactions.objects.count(), 2)
