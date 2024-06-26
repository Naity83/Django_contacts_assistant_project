import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

def main(request):
    return render(request, 'contacts/index.html')

@login_required
def contact_list(request):
    query = request.GET.get('search')
    if query:
        contacts = Contact.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(address__icontains=query) |
            Q(email__icontains=query),
            user=request.user  # Добавлено фильтрация по пользователю
        )
    else:
        contacts = Contact.objects.filter(user=request.user)  # Добавлено фильтрация по пользователю
    
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/contact_list.html', context)


@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user  # Присваивание текущего пользователя
            contact.save()
            logger.info('Contact created successfully')
            return redirect('contacts:contact_list')
        else:
            logger.error('Form is not valid')
            logger.error(form.errors)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})


@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)  # Добавлено фильтрация по пользователю
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)  # Добавлено фильтрация по пользователю
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    # Обработка GET запроса для отображения страницы удаления контакта
    return render(request, 'contacts/contact_delete.html', {'contact': contact})

@login_required
def upcoming_birthdays(request):
    if request.method == 'GET':
        interval = request.GET.get('interval')
        if not interval:
            return HttpResponseBadRequest("Parameter 'interval' is required.")
        
        try:
            days = int(interval)
        except ValueError:
            return HttpResponseBadRequest("Parameter 'interval' must be an integer.")

        upcoming_contacts = Contact.get_upcoming_birthdays(days, request.user)
        return render(request, 'contacts/contact_list.html', {'contacts': upcoming_contacts})
    else:
        return HttpResponseBadRequest("Only GET requests are allowed.")