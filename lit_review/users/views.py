from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm, FollowForm
from .models import User, UserFollows


def authenticate_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request, "identifiants incorrects")
    return render(request, "users/authenticate.html", context={"form": form})


def signup_page(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "users/signup.html", context={"form": form})


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def get_followed_users(user):
    return user.following.all()


def get_following_by_users(user):
    return user.followed_by.all()


@login_required
def follow_page(request):
    search_form = FollowForm()
    if request.method == "POST":
        if "unfollow" in request.POST:
            print(f"unfollow {request.POST['unfollow']}")
            given_relation = request.POST['unfollow']
            if request.user.following.filter(id=given_relation).first():
                UserFollows.objects.get(id=given_relation).delete()
        else:
            search_form = FollowForm(request.POST)
            if search_form.is_valid():
                given_username = search_form.cleaned_data["username"]
                given_user = User.objects.filter(username=given_username).first()
                if (given_username != request.user and
                        given_user and
                        len(request.user.following.filter(followed_user=given_user)) == 0):
                    UserFollows(user=request.user, followed_user=given_user).save()
                else:
                    print("PAS OK")
            else:
                print("Pas OK")
    return render(request, "users/follow.html",
                  context=
                  {
                      "search_form": search_form,
                      "followed": get_followed_users(request.user),
                      "following_by": get_following_by_users(request.user)
                  })
