from django.db import models
from uuid import uuid4
from users.models import UserProfile


def generate_guid():
    return uuid4().hex


class Lock(models.Model):
    lock_statuses = (('active', 'Active'), ('inactive', 'Inactive'), ('locked', 'Locked'), ('unlocked', 'Unlocked'), ('maintenance', 'Maintenance'))

    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True)
    status = models.CharField(max_length=16, choices=lock_statuses, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='lock_created_by')
    updated_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, null=True, related_name='lock_updated_by')

    class Meta:
        db_table = "locks"
