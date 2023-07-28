from django.forms import Form, CharField, PasswordInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(Form):
    username = CharField(max_length=63, label='Nom d’utilisateur')
    password = CharField(max_length=63, widget=PasswordInput, label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class FollowForm(Form):
    username = CharField(max_length=63, label='Nom d’utilisateur')
