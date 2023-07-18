from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

import uuid

class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlists')
    active = models.BooleanField(default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.rating)