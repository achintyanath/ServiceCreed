from django.db.models import fields
from django.db.models.fields import CommaSeparatedIntegerField
from rest_framework import serializers
from .models import Category, Customer, PaymentDetails, Service, ServiceProvider,  Order



class CustomerSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture','isSubscribed','subscriptionPeriod','date']

class CustomerSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture']

class ServiceProviderSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture','category','services','cost']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','categoryName','categoryImage']


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Service
        fields = ['id','category','serviceName', 'description','serviceImage']

class ServiceSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','serviceName', 'category', 'description','serviceImage']

class ServiceProviderSerializerGet(serializers.ModelSerializer):

    services = ServiceSerializer()
    class Meta:
        model = ServiceProvider
        fields = ['id','username','fullName','email', 'password', 'address', 'mobileNumber', 'profilePicture','services','cost']
        depth = 1


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
    customer = CustomerSerializerGet()
    paymentDetails=PaymentDetailsSerializerGet()

    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']
        depth =1

class OrderSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']
        


