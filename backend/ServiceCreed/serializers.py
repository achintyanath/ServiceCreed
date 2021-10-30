from django.db.models.fields import CommaSeparatedIntegerField
from rest_framework import serializers
from .models import Customer, PaymentDetails, Service, ServiceProvider,  Order



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username','email', 'password', 'address', 'mobileNumber', 'profilePicture']

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id','username','email', 'password', 'address', 'mobileNumber', 'profilePicture']

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['id','serviceName', 'description']

class OrderSerializerGet(serializers.ModelSerializer):
    provider=ServiceProvider
    customer = Customer
    paymentDetails=PaymentDetails

    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']

class OrderSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','provider', 'customer', 'paymentDetails']
        

class PaymentDetailsSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['id','amount', 'date','status', ' paymentMethod']

class PaymentDetailsSerializerElse(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['id','amount' ,'status', ' paymentMethod']
        depth=1
