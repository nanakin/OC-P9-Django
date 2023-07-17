from django.shortcuts import render
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from .models import Ticket


def get_users_viewable_tickets(username):
    tickets = Ticket.objects.filter(user=username)
    return tickets


@login_required()
def stream_page(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(tickets, key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/stream.html", context={'posts': posts})
