from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.TextField(max_length=2048, blank=True)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Review(models.Model):

    class Rating(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    headline = models.fields.CharField(max_length=128)
    body = models.fields.TextField(max_length=8192, blank=True)
    rating = models.fields.IntegerField(choices=Rating.choices, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user')
