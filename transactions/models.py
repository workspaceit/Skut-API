from django.db import models
from uuid import uuid4
from users.models import UserProfile
from rides.models import Ride


def generate_guid():
    return uuid4().hex


class Transaction(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    amount = models.CharField(unique=True, max_length=50)
    status = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    ride = models.ForeignKey(to=Ride, on_delete=models.CASCADE)

    class Meta:
        db_table = "transactions"
