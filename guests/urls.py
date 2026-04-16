from .views import guestsList, addGuest, editGuest
from django.urls import path

urlpatterns = [
    path('', guestsList, name="guestsList"),
    path('addGuest', addGuest, name="addGuest"),
    path('guestsList/<int:guest_id>/edit', editGuest, name="editGuest"),
]