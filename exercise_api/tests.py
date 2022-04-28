from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.
# ref: https://www.django-rest-framework.org/api-guide/testing/
factory = APIRequestFactory()
get_points_request = factory.get('/points')
get_transactions_request = factory.get('/transaction')
first_call = {"payer": "DANNON", "points": 1000,
              "timestamp": "2020-11-02T14:00:00Z"}
second_call = {"payer": "UNILEVER", "points": 200,
               "timestamp": "2020-10-31T11:00:00Z"}
third_call = {"payer": "DANNON", "points": -
              200, "timestamp": "2020-10-31T15:00:00Z"}
fourth_call = {"payer": "MILLER COORS", "points": 10000,
               "timestamp": "2020-11-01T14:00:00Z"}
fifth_call = {"payer": "DANNON", "points": 300,
              "timestamp": "2020-10-31T10:00:00Z"}

first_post_request = factory.post(
    '/add-transaction', first_call, format='json')
second_post_request = factory.post(
    '/add-transaction', second_call, format='json')
third_post_request = factory.post(
    '/add-transaction', third_call, format='json')
fourth_post_request = factory.post(
    '/add-transaction', fourth_call, format='json')
fifth_post_request = factory.post(
    '/add-transaction', fifth_call, format='json')
