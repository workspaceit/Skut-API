from django.db import models
from uuid import uuid4
from scooters.models import Scooter
from users.models import UserProfile
from stands.models import Stand
from django.contrib.postgres.fields import ArrayField


def generate_guid():
    return uuid4().hex


class Ride(models.Model):
    ride_statuses = (
        ('reserved', 'Reserved'), ('riding', 'Riding'), ('paused', 'Paused'),
        ('completed', 'Completed'), ('canceled', 'Canceled')
    )

    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    status = models.CharField(max_length=16, choices=ride_statuses, default='riding')
    start_time = models.DateTimeField(null=True, auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    start_location = models.CharField(max_length=64, null=True)
    end_location = models.CharField(max_length=64, null=True)
    start_stand = models.ForeignKey(to=Stand, on_delete=models.SET_NULL, null=True, related_name='ride_start_stand')
    end_stand = models.ForeignKey(to=Stand, on_delete=models.SET_NULL, null=True, related_name='ride_end_stand')
    riding_path = ArrayField(base_field=models.CharField(max_length=64), null=True)
    distance = models.FloatField(default=0)
    charge = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    scooter = models.ForeignKey(to=Scooter, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "rides"

