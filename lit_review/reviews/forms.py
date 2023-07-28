from django.forms import ModelForm, BooleanField, HiddenInput, RadioSelect
from .models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre"}


class EditTicketForm(TicketForm):
    edit_ticket = BooleanField(widget=HiddenInput, initial=True)


class DeleteTicketForm(TicketForm):
    delete_ticket = BooleanField(widget=HiddenInput, initial=True)

    class Meta(TicketForm.Meta):
        fields = []


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        rating_choices = zip([i for i in range(0, 6)], [str(i) for i in range(0, 6)])
        widgets = {
            "rating": RadioSelect(choices=rating_choices)
        }
        labels = {"headline": "Titre",
                  "rating": "Note",
                  "body": "Commentaire"}


class EditReviewForm(ReviewForm):
    edit_ticket = BooleanField(widget=HiddenInput, initial=True)


class DeleteReviewForm(ReviewForm):
    delete_ticket = BooleanField(widget=HiddenInput, initial=True)

    class Meta(ReviewForm.Meta):
        fields = []
