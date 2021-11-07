from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class AppUser(AbstractUser):

    username=models.CharField(max_length=100,unique=True,null=False)
    fullName = models.CharField(max_length=200,default = 'John Doe', null =False)
    email = models.EmailField(max_length=254)
    password =  models.CharField(max_length=100)
    address = models.CharField(max_length=500,null=True)
    mobileNumber=  PhoneNumberField()
    profilePicture =models.ImageField(upload_to='appuser', default= 'default.png')

    def __str__(self):
         return f"{self.username}"


class Category(models.Model):
    categoryName = models.CharField( max_length=50)
    categoryImage = models.ImageField(upload_to='category',default = 'default.jpeg')
    def __str__(self):
        return f"{self.categoryName}"
   

class Service(models.Model):
    category = models.ForeignKey(Category,on_delete=CASCADE, default=1)
    serviceName = models.CharField( max_length=50)
    description =models.CharField( max_length=200)
    serviceImage = models.ImageField(upload_to='service',default = 'default.jpeg')
    def __str__(self):
        return f"{self.serviceName}"

class Customer(AppUser):
    isSubscribed = models.BooleanField(default=False)
    subscriptionPeriod = models.CharField(
        max_length=16,
        null=True
    )
    date = models.DateField(null = True)
    #myorders are specified using the related_name in Order Model : myCustomerOrders
   

class ServiceProvider(AppUser):
    category = models.ForeignKey(Category,on_delete=CASCADE,default=1)
    services = models.ForeignKey(Service,related_name="providers_in_given_category",on_delete=CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0,null=False)
    #orderrecived is accessed by related_name in Order Model:  myServiceOrders
    def __str__(self):
        return f"{self.username}"
gi


class PaymentDetails(models.Model):
    amount  = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=False)
    date = models.DateTimeField(auto_now=True)
    class statusChoices(models.TextChoices):
        SUCCESS = 'Successfull'
        FAIL = 'Failed'
    status = models.CharField(
        max_length=16,
        choices=statusChoices.choices
    )
    class paymentMethodChoices(models.TextChoices):
        CARD = 'Debit Card/Credit Card'
        CASH = 'Cash on Delivery'
    paymentMethod = models.CharField(
        max_length=25,
        choices=paymentMethodChoices.choices
    )

    def __str__(self):
        return f"{self.amount} {self.date} {self.status} "

class Order(models.Model):
    provider = models.ForeignKey(ServiceProvider,related_name="myServiceOrders",on_delete=CASCADE)
    customer = models.ForeignKey(Customer,related_name="myCustomerOrders",on_delete=CASCADE)
    paymentDetails = models.ForeignKey(PaymentDetails,related_name ="paymentdetails", on_delete=CASCADE)


