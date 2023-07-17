from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def authenticate_page(request):
    return render(request, "users/authenticate.html")


def login_page(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "users/login.html", context={"form": form})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            print("invalid form")
    return render(request, "users/signup.html", context={"form": form})


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
