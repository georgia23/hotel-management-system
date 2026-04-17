from django.urls import path
from .views import reportView

urlpatterns = [
    path('reports/', reportView, name='reports'),    
]