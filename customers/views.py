from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from .models import Customer
from .serializers import CustomerSerializer
from .authentication import create_access_token, create_refresh_token
# Create your views here.


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['post'], detail=False, url_path="register")
    def register(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path="login")
    def login(self, request):
        customer = Customer.objects.filter(email=request.data['email']).first()

        if customer is None:
            raise APIException("Username or password is incorrect")

        if not customer.check_password(request.data['password']):
            raise APIException("Username or password is incorrect")

        access_token = create_access_token(customer.id)
        refresh_token = create_refresh_token(customer.id)

        response = Response()
        response.set_cookie(key='refreshToken',
                            value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token
        }

        return response
