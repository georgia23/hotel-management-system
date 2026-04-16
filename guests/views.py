from django.shortcuts import redirect, render

from .forms import GuestForm
from .models import Guest

# Create your views here.

def guestsList(request):
    guests = Guest.objects.all()

    context = {
        'guests': guests
    }
    return render(request, 'guestsList.html', context)

def addGuest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestsList')
    else:        
        form = GuestForm()

    return render(request, 'addGuest.html', {'form': form})

def editGuest(request, guest_id):
    guest = Guest.objects.get(id=guest_id)

    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guestsList')
    else:
        form = GuestForm(instance=guest)

    return render(request, 'addGuest.html', {'form': form})
