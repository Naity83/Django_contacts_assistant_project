import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

logger = logging.getLogger(__name__)

def main(request):
    return render(request, 'contacts/index.html')

def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

import logging
from django.shortcuts import render, redirect
from .forms import ContactForm

logger = logging.getLogger(__name__)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            logger.info('Contact created successfully')
            return redirect('contacts:contact_list')
        else:
            logger.error('Form is not valid')
            logger.error(form.errors)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

def upcoming_birthdays(request, days):
    upcoming_contacts = Contact.get_upcoming_birthdays(days)
    return render(request, 'contacts/upcoming_birthdays.html', {'upcoming_contacts': upcoming_contacts})

