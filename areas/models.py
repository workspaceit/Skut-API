from django.contrib.postgres.fields import JSONField
from django.db import models
from uuid import uuid4


def generate_guid():
    return uuid4().hex


class Area(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True)
    area_shape = JSONField(default=dict({"geometry": {}}))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "areas"

    def __str__(self):
        return self.name
