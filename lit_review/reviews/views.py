from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from itertools import chain
from .models import Ticket, Review
from .forms import TicketForm, EditTicketForm, DeleteTicketForm, ReviewForm
from django.db.models import Q


def get_followed_users(user):
    return user.following.all().values_list("followed_user")


def get_users_viewable_tickets(user):
    return Ticket.objects.filter(
        Q(user=user) |
        Q(user__in=get_followed_users(user)))


def get_users_tickets(user):
    return user.tickets.all()


def get_users_viewable_reviews(user):
    return Review.objects.filter(
        Q(user=user) |
        Q(user__in=get_followed_users(user)) |
        Q(ticket__in=get_users_tickets(user)))


def get_users_reviews(user):
    return user.reviews.all()


def get_users_answerable_tickets(user):
    return Ticket.objects.filter(~Q(id__in=user.reviews.values_list("ticket")))


@login_required()
def my_activity_page(request):
    tickets = get_users_tickets(request.user)
    reviews = get_users_reviews(request.user)
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/my_activity.html", context={'posts': posts})


@login_required()
def feed_page(request):
    tickets = get_users_viewable_tickets(request.user)
    reviews = get_users_viewable_reviews(request.user)
    answerable = get_users_answerable_tickets(request.user)
    print(f"{answerable=}")
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/feed.html", context={'posts': posts, 'answerable': answerable})


@login_required()
def add_ticket_page(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')
    return render(request, "reviews/add_ticket.html", context={"form": form})


@login_required()
def edit_ticket_page(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket not in get_users_tickets(request.user):
        return redirect("feed")
    edit_form = EditTicketForm(instance=ticket)
    delete_form = DeleteTicketForm(instance=ticket)
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_form = EditTicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
        elif "delete_ticket" in request.POST:
            delete_form = DeleteTicketForm(request.POST, instance=ticket)
            if delete_form.is_valid():
                ticket.delete()
        return redirect('feed')
    return render(request, "reviews/edit_ticket.html",
                  context={"edit_form": edit_form, "delete_form": delete_form})


@login_required()
def add_review_page(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket not in get_users_answerable_tickets(request.user):
        redirect("feed")
    else:
        form = ReviewForm()
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.save()
                return redirect('feed')
        return render(request, "reviews/add_review.html", context={"form": form})
