from django.shortcuts import render, redirect
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from itertools import chain
from .models import Ticket, Review, UserFollows
from .forms import TicketForm
from django.db.models import Q


def get_followed_users(user):
    return UserFollows.objects.filter(user=user).values_list("followed_user")


def get_users_viewable_tickets(user):
    tickets = Ticket.objects.filter(
        Q(user=user) |
        Q(user__in=get_followed_users(user)))
    return tickets


def get_users_viewable_reviews(user):
    reviews = Review.objects.filter(
        Q(user=user) |
        Q(user__in=get_followed_users(user)) |
        Q(ticket__in=Ticket.objects.filter(user=user)))
    return reviews


@login_required()
def stream_page(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/stream.html", context={'posts': posts})


@login_required()
def add_ticket_page(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('stream')
    return render(request, "reviews/add_ticket.html", context={"form": form})
