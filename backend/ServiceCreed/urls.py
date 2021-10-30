from django.urls import path
from ServiceCreed.views import CustomerViewSet, ServiceProviderViewSet, ServiceViewSet, OrderViewSet, PaymentDetailsViewSet,loginrequest, logoutrequest
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'serviceprovider', ServiceProviderViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'order', OrderViewSet)
router.register(r'paymentdetail', PaymentDetailsViewSet)

urlpatterns = [
    path('login',csrf_exempt(loginrequest),name='loginrequest'),
    path('logout',csrf_exempt(logoutrequest),name='logoutrequest'),
]
urlpatterns+=router.urls
