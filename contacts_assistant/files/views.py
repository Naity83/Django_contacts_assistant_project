from django.shortcuts import render, redirect

from .forms import MyFileForm
from .models import MyFile


def index(request):
    return render(request, 'files/index.html', context={"msg": "Hello world!"})


def all_files(request):
    my_files = MyFile.objects.all()
    return render(request, 'files/files.html', context={"files": my_files})


def upload(request):
    form = MyFileForm(instance=MyFile())
    if request.method == 'POST':
        form = MyFileForm(request.POST, request.FILES, instance=MyFile())
        if form.is_valid():
            form.save()
            return redirect(to="files:files")
    return render(request, 'files/upload.html', context={"form": form})
