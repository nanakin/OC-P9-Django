from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # name and inheritance fixed by OC
    first_name = None
    last_name = None
    email = None
