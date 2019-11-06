from django.db import models
from uuid import uuid4
from areas.models import Area
from users.models import UserProfile


def generate_guid():
    return uuid4().hex


class Stand(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    name = models.CharField(max_length=255)
    coordinate = models.CharField(max_length=64, null=True)
    area = models.ForeignKey(to=Area, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='stand_created_by')
    updated_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='stand_updated_by')

    class Meta:
        db_table = "stands"
