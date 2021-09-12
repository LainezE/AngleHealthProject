from collections import namedtuple
from copy import error
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import \
    APIView  # Used so normal views returns API data

from .models import Products
from .serializers import ProductSerializer

# Create your views here.

class ProductList(APIView):
    """ProductList object contains methods for a Post and Search route"""
    
    def get(self, request):
        """Search Route method. If there are no parameters in the url, function returns all products"""
        try:
            keyword = request.query_params['keyword']
            min_price = request.query_params['min_price']
            max_price = request.query_params['max_price']

            if(min_price.isdigit()) and max_price.isdigit(): #Upper and Lower bound 
                products = Products.objects.filter(name__icontains=keyword, price__range=(min_price,max_price))
            elif min_price.isdigit() and not(max_price.isdigit()): #No upper bound 
                products = Products.objects.filter(name__icontains=keyword, price__gte=min_price)
            elif not(min_price.isdigit()) and max_price.isdigit(): #No lower bound 
                products = Products.objects.filter(name__icontains=keyword, price__lte=max_price)
            else: #No upper or lower bound 
                products = Products.objects.filter(name__icontains=keyword)

            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)
        except: 
            products = Products.objects.all()
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)
    
    def post(self, request):
        """Post route method. Input is in json form"""
        if (self.validatePost(request.data["posts"])):
            serializer = ProductSerializer(data=request.data['posts'], many=True)
            serializer.is_valid()
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def validatePost(self, productlist):
        """validatePost(self, list) function takes in a list to make sure all post information is valid. Returns Boolean value """
        for product in productlist:
            # name must be between 4 and 10 characters inclusive 
            if len(product['name']) < 4 or len(product['name']) > 10:
                print("name must be between 4 and 10 characters inclusive")
                return False

            #First character of name must be a digit or letter 
            firstchar = product['name'][0]
            if not(firstchar.isalpha()) and not(firstchar.isdigit()):
                print("First character of name must be a digit or letter: " + firstchar)
                return False

            #Other letters must be digit, letter, hyphen, or space 
            allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -"))
            validation = set(product['name'])
            if not(validation.issubset(allowed_chars)):
                print("Other letters must be digit, letter, hyphen, or space ")
                return False

            #Price must be an integer
            if not(isinstance(product['price'], int)):
                print("Price must be an integer")
                return False

            #start_date must be in form dd/mm/yyyy
            requiredformat = "%m/%d/%Y"
            try:
                start_date =datetime.strptime(product['start_date'], requiredformat)
            except ValueError:
                print("start_date for " + product['name'] + " " + "must be in format dd/mm/yyyy")
                return False

            #Date has to be today or in the future
            if(datetime.today() > start_date):
                print("Date has to be today or in the future ")
                return False
            
            #Name cannot already exist inside the database if some_queryset.filter(pk=entry.pk).exists():
            if(Products.objects.filter(name=product['name']).exists()):
                print("Product Name Already Exists")
                return False
        return True
