from django.shortcuts import render
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from itertools import chain
from .models import Ticket, Review
from django.db.models import Q


def get_users_viewable_tickets(username):
    tickets = Ticket.objects.filter(user=username)
    return tickets


def get_users_viewable_reviews(username):
    reviews = Review.objects.filter(Q(user=username) | Q(ticket__in=Ticket.objects.filter(user=username)))
    return reviews


@login_required()
def stream_page(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/stream.html", context={'posts': posts})
