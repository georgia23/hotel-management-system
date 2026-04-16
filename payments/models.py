from django.db import models
from rooms.models import Room

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    payment_date = models.DateTimeField(blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} on {self.payment_date.strftime('%Y-%m-%d %H:%M:%S')} via {self.payment_type}"
