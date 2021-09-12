import json

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class ProductTestCase(APITestCase):

    def test_postRoute_pass(self):

        filedata = open("ecommerce/data_01.json", "r")
        testdata = json.loads(filedata.read())

        response = self.client.post(
            '/products/', json.dumps(testdata), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_postRoute_fail(self):
        
        filedata = open("ecommerce/data_03.json", "r")
        testdata = json.loads(filedata.read())

        response = self.client.post(
            '/products/', json.dumps(testdata), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_searchRoute_pass1(self):
        testurl = "http://localhost:8000/products/?keyword=a&min_price=0&max_price=100"
        response = self.client.get(testurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_searchRoute_pass2(self):
        testurl = "http://localhost:8000/products/?keyword=a&min_price=0&max_price="
        response = self.client.get(testurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_searchRoute_pass3(self):
        testurl = "http://localhost:8000/products/?keyword=a&min_price=&max_price=100"
        response = self.client.get(testurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_searchRoute_pass4(self):
        testurl = "http://localhost:8000/products/?keyword=a&min_price=&max_price="
        response = self.client.get(testurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_searchRoute_fail(self):
        testurl = "http://localhost:8000/products/?keyword=elilainez&min_price=0&max_price=100"
        response = self.client.get(testurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
