from django.urls import path
from .views import paymentsList, makePayment

urlpatterns = [
    path('', paymentsList, name="paymentsList"),
    path('makePayment', makePayment, name="makePayment")
]