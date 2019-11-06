from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


def generate_guid():
    return uuid4().hex


class UserProfile(models.Model):
    """here phone number will be username"""

    uid = models.CharField(primary_key=True, max_length=32, default=generate_guid)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=32, unique=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    registration_code = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    def delete(self, using=None, keep_parents=False):
        """ User deletion will delete UserProfile too """
        return self.user.delete()

    class Meta:
        db_table = "user_profiles"
