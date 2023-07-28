from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(AbstractUser):  # name and inheritance fixed by OC
    first_name = None
    last_name = None
    email = None


class UserFollows(models.Model):  # name and inheritance fixed by OC, content suggested in the UML diagram
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by'
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = (
            'user',
            'followed_user',
        )  # fixed by OC

    def __str__(self):
        return f"{self.user} > {self.followed_user}"

    def __repr__(self):
        return f"{self.user} > {self.followed_user}"
