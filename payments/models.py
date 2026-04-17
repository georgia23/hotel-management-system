from django.db import models
from rooms.models import Room
from guests.models import Guest

# Create your models here.
class Payment(models.Model):
    PAYMENT_CHOICES = [
            ('Mobile Money', 'Mobile Money'),
            ('Cash', 'Cash'),
        ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    payment_date = models.DateTimeField(blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} on {self.payment_date.strftime('%Y-%m-%d %H:%M:%S')} via {self.payment_type}"
