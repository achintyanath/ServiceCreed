import datetime
from django.shortcuts import render
from rest_framework.response import Response
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect
import requests
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import AppUser, Category, Customer,ServiceProvider,Service, Order,PaymentDetails
from .serializers import CategorySerializer, CustomerSerializerElse, CustomerSerializerGet, ServiceSerializer,  ServiceProviderSerializerElse,ServiceProviderSerializerGet, OrderSerializerGet, OrderSerializerElse, PaymentDetailsSerializerGet, PaymentDetailsSerializerElse
from rest_framework import viewsets
from django.contrib.auth import  login, logout
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view(["POST","GET"])
@permission_classes([AllowAny])
def loginrequest(request):
    print(request)
    username = request.data["username"]
    password = request.data["password"]

    try:
        appuser= AppUser.objects.get(username = username)
        storedPassword = appuser.password
        if(storedPassword==password):
            login(request,appuser)
            refresh = RefreshToken.for_user(appuser)
            res =  {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'userId': appuser.id,
                    'status' : "verified"
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            res= {
                'status' : "Wrong Password"
            }
            return Response(res,status = status.HTTP_401_UNAUTHORIZED)


    except: 
        res = {
            'status' : "User Not Found"
        }

        return Response(res, status = status.HTTP_404_NOT_FOUND )
    

def logoutrequest(request):
    logout(request)
    res ={
        'status' :"loggedout"
    }
    return HttpResponse(res)


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    def get_serializer_class(self):
        if self.action == 'get' or self.action=='list' or self.action=='retrieve' :
            return CustomerSerializerGet
        else:
            return CustomerSerializerElse
    def get_permissions(self):
        if self.action == 'post' or self.action=='patch' or self.action=='put' :
            permission_classes =[AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(methods=['get'],detail = False,url_path='check',url_name='check',permission_classes=[AllowAny])
    def check(self,request):
        #check if the user is logged in or not
        #url : http://127.0.0.1:8000/customer/check
        if(request.user.is_authenticated):
            customer= Customer.objects.get(username = request.user)
            serializer = CustomerSerializerElse(customer)
            return Response(serializer.data,status=status.HTTP_200_OK)

        else: 
            res ={
                "status" : "not verified"
            }
            return Response(res,status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['GET'],detail = True, url_path='myorders',url_name = 'url_name',permission_classes=[AllowAny])
    def myorder(self,request,pk):
        print(pk)
        myorders = Order.objects.filter(customer=pk)
        myodersRes = OrderSerializerGet(myorders,many =True)
        return Response(myodersRes.data,status=status.HTTP_200_OK)
    
    @action(methods=['POST'],detail = True, url_path='subs',url_name = 'subs',permission_classes=[AllowAny])
    def subscription(self,request,pk) :
        print(request.data)
        customer = Customer.objects.filter(id = pk)
        customer.update(isSubscribed = True)
        customer.update(subscriptionPeriod = request.data["duration"])
        customer.update(date = datetime.datetime.now())
        res= {
            'status' : 'done'
        }
     
        return Response(res)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    def get_serializer_class(self):
        if self.action == 'get' or self.action=='list' or self.action=='retrieve' :
            return ServiceProviderSerializerGet
        else:
            return ServiceProviderSerializerElse

    def get_permissions(self):
        if self.action == 'post' or self.action=='patch' or self.action=='put' :
            permission_classes =[AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(methods=['get'],detail = False,url_path='check',url_name='check',permission_classes=[AllowAny])
    def check(self,request):
        #check if the user is logged in or not
        #url : http://127.0.0.1:8000/customer/check
        if(request.user.is_authenticated):
            customer= ServiceProvider.objects.get(userName = request.user)
            return Response(customer,status=status.HTTP_200_OK)

        else: 
            res ={
                "status" : "not verified"
            }
            return Response(res,status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['GET'],detail = True, url_path='myorders',url_name = 'url_name',permission_classes=[AllowAny])
    def myorder(self,request,pk):
        print(pk)
        myorders = Order.objects.filter(provider=pk)
        myodersRes = OrderSerializerGet(myorders,many =True)
        return Response(myodersRes.data,status=status.HTTP_200_OK)
    
    
class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    def get_serializer_class(self):
        if self.action == 'get' or self.action=='list' or self.action=='retrieve' :
            return OrderSerializerGet
        else:
            return OrderSerializerElse
    permission_classes = [AllowAny]


class PaymentDetailsViewSet(viewsets.ModelViewSet):

    queryset = PaymentDetails.objects.all()    
    def get_serializer_class(self):
        if self.action == 'get' or self.action=='list' or self.action=='retrieve' :
            return PaymentDetailsSerializerGet
        else:
            return PaymentDetailsSerializerElse
    permission_classes = [AllowAny]
# Create your views here.
