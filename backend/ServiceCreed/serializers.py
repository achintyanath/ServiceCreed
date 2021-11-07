from django.db.models import fields
from django.db.models.fields import CommaSeparatedIntegerField
from rest_framework import serializers
from .models import Category, Customer, PaymentDetails, Service, ServiceProvider,  Order



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture']

class ServiceProviderSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture','category','services','cost']

class ServiceProviderSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = ServiceProvider
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture','category','services','cost']
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','categoryName','categoryImage']


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Service
        fields = ['id','category','serviceName', 'description','serviceImage']

class PaymentDetailsSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['id','amount', 'date','status', 'paymentMethod']
      

class PaymentDetailsSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['id','amount' ,'status', 'paymentMethod']

class OrderSerializerGet(serializers.ModelSerializer):
    provider=ServiceProviderSerializerGet()
    customer = CustomerSerializer()
    paymentDetails=PaymentDetailsSerializerGet()

    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']
        depth =1

class OrderSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']
        


