from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # name and inheritance fixed by OC
    first_name = None
    last_name = None
    email = None
    pass


"""temporary commented
class UserFollows(models.Model):  # name and inheritance fixed by OC
    # Your UserFollows model definition goes here

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )  # fixed by OC
"""