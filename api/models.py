from django.db import models
from django.utils.translation import gettext_lazy as _

# The first element in each tuple is the actual value to be set on the model, 
# and the second element is the human-readable name. 
class LockerStatus(models.TextChoices):
    OPEN = "OPEN", _("Open")
    CLOSED = "CLOSED", _("Closed")

class RentSize(models.TextChoices):
    XS = "XS", _("XS")
    S = "S", _("S")
    M = "M", _("M")
    L = "L", _("L")
    XL = "XL", _("XL")

class RentStatus(models.TextChoices):
    CREATED = "CREATED", _("Created")
    WAITING_DROPOFF = "WAITING_DROPOFF", _("Waiting Drop-off")
    WAITING_PICKUP = "WAITING_PICKUP", _("Waiting Pick-up")
    DELIVERED = "DELIVERED", _("Delivered")

class Bloq(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title

class Locker(models.Model):
    bloq = models.ForeignKey(Bloq, on_delete=models.CASCADE, related_name='lockers')
    status = models.CharField(max_length=50, choices=LockerStatus.choices, default=LockerStatus.OPEN,)
    isOccupied = models.BooleanField()

    def __str__(self):
        return "%s - %s" % (self.bloq.title, self.status)


class Rent(models.Model):
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name='rents')
    weight = models.FloatField()
    size = models.CharField(max_length=50, choices=RentSize.choices, default=RentSize.XS,)
    status = models.CharField(max_length=50, choices=RentStatus.choices, default=RentStatus.CREATED,)
    createdAt = models.DateTimeField(auto_now_add=True)
    droppedOffAt = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    pickedUpAt = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return "%s - %s" % (self.size, self.status)
    
