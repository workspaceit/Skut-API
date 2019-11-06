from django.db import models
from uuid import uuid4
from users.models import UserProfile


def generate_guid():
    return uuid4().hex


class Setting(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    key = models.CharField(unique=True, max_length=50)
    value = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='setting_created_by')
    updated_by = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='setting_updated_by')

    class Meta:
        db_table = "settings"
