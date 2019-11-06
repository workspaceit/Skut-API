from django.db import models
from uuid import uuid4
from users.models import UserProfile
from scooter_models.models import ScooterModel
from stands.models import Stand
from locks.models import Lock


def generate_guid():
    return uuid4().hex


def generate_scooter_name():
    return "SKUT-{}".format(uuid4().hex)


class Scooter(models.Model):
    scooter_statuses = (('active', 'Active'), ('inactive', 'Inactive'), ('riding', 'Riding'), ('maintenance','Maintenance'))

    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    key_name = models.CharField(max_length=64, default=generate_scooter_name, unique=True)
    description = models.CharField(max_length=512, null=True)
    image = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=16, choices=scooter_statuses, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    model = models.ForeignKey(to=ScooterModel, on_delete=models.CASCADE)
    lock = models.ForeignKey(to=Lock, on_delete=models.SET_NULL, null=True)
    stand = models.ForeignKey(to=Stand, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='scooter_created_by')
    updated_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='scooter_updated_by')

    class Meta:
        db_table = "scooters"
