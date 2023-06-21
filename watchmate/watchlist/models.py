from django.db import models

import uuid


class Movie(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name