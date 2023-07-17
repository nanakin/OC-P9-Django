from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def stream_page(request):
    return render(request, "reviews/stream.html")
