from django.shortcuts import render
from payments.models import Payment
from rooms.models import Room
from guests.models import Guest
from django.db.models import Sum

# Create your views here.

def reportView(request):

    payments = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0   
    rooms = Room.objects.count()
    guests = Guest.objects.count()
    context = {
        'total_payments': payments,
        'total_rooms': rooms,
        'total_guests': guests,
    }
    return render(request, 'reports.html', context)
