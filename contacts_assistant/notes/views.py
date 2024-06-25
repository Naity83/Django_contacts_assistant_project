from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TagForm, NoteForm
from .models import Tag, Note


# Create your views here.
@login_required
def notes_main(request):
    notes = Note.objects.filter(user=request.user).all()
    query = request.GET.get('search')

    if query:
        notes = notes.filter(
                            Q(name__icontains=query) |
                            Q(description__icontains=query) |
                            Q(tags__name__icontains=query)
                            )

    return render(request, 'notes/note_base.html', {"notes": notes})


@login_required
def add_tag(request):
    tags = Tag.objects.filter(user=request.user).all()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='notes:note_add')
        else:
            return render(request, 'notes/tag_add.html', {"tags": tags, 'form': form})

    return render(request, 'notes/tag_add.html', {"tags": tags, 'form': TagForm()})


@login_required
def note_add(request):
    tags = Tag.objects.filter(user=request.user).all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)
            return redirect(to='notes:notes_main')
        else:
            return render(request, 'notes/note_add.html', {"tags": tags, 'form': form})

    return render(request, 'notes/note_add.html', {"tags": tags, 'form': NoteForm()})


@login_required
def delete_note(request, pk):
    note = Note.objects.filter(pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect(to='notes:notes_main')


@login_required
def note_update(request, pk):
    tags = Tag.objects.filter(user=request.user).all()
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            update_note = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            for tag in choice_tags.iterator():
                update_note.tags.clear()
                update_note.tags.add(tag)
            return redirect('notes:notes_main')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_update.html', {"tags": tags, 'form': form})
