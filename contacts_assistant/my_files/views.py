# from django.shortcuts import render, redirect
# import cloudinary
# from .forms import MyFileForm
# from .models import MyFile

from django.shortcuts import render, redirect, get_object_or_404
from .models import MyFile
from .forms import MyFileForm


def upload_file(request):
    if request.method == 'POST':
        form = MyFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = MyFileForm()
    return render(request, 'files/upload_files.html', {'form': form})


def file_list(request):
    files = MyFile.objects.all()
    sort_by = request.GET.get('sort_by', 'name')
    order = request.GET.get('order', 'asc')
    if order == 'desc':
        sort_by = '-' + sort_by
    files = files.order_by(sort_by)
    return render(request, 'files/files.html', {'files': files})


def delete_file(request, pk):
    file = get_object_or_404(MyFile, pk=pk)
    file.delete()
    return redirect('file_list')
