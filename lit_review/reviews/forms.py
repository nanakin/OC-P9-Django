from django.forms import ModelForm, BooleanField, HiddenInput
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class EditTicketForm(TicketForm):
    edit_ticket = BooleanField(widget=HiddenInput, initial=True)


class DeleteTicketForm(TicketForm):
    delete_ticket = BooleanField(widget=HiddenInput, initial=True)

    class Meta(TicketForm.Meta):
        fields = []
