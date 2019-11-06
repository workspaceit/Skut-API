from django.db import models
from uuid import uuid4
from users.models import UserProfile


def generate_guid():
    return uuid4().hex


class Notification(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    title = models.CharField(max_length=128)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "notifications"
