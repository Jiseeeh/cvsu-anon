import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AnonUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    client_ip = models.GenericIPAddressField(null=True)
    ray_points = models.IntegerField(default=0)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        AnonUser, on_delete=models.CASCADE, related_name='sender_id', null=True)
    # NO NEED TO NAME SOMETHING_ID
    receiver_id = models.ForeignKey(
        AnonUser, on_delete=models.CASCADE, related_name='receiver_id')
    message = models.TextField(null=False)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
