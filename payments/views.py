from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm

# Create your views here.
def paymentsList(request):
    payments = Payment.objects.all()

    context = {
        'payments': payments
    }
    return render(request, 'paymentsList.html', context)

def makePayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paymentsList')
    else:        
        form = PaymentForm()

    return render(request, 'makePayment.html', {'form': form})
