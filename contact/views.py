from django.views.generic import CreateView
from contact.forms import ContactForm
from contact.models import Contact
from contact.tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)