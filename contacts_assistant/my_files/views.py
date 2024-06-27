from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PictureForm, VideoForm, DocumentForm
from .models import Picture, Video, Document
import cloudinary.uploader
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
@login_required
def main(request):
    pictures = Picture.objects.filter(user=request.user)
    videos = Video.objects.filter(user=request.user)
    documents = Document.objects.filter(user=request.user)
    return render(request, 'my_files/files_title.html', {
        'pictures': pictures,
        'videos': videos,
        'documents': documents,
    })


@login_required
def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user

            # Загрузка изображения в Cloudinary
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Используем request.FILES['path'] для правильного пути к изображению
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME']
                )

                # Сохранение URL изображения Cloudinary в вашу модель
                picture.path = upload_result['url']  # Обновите path с URL из Cloudinary
                picture.save()

                return redirect('my_files:home')

            except Exception as e:
                # Обработка ошибок загрузки
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')

        # Если форма не прошла валидацию
        else:
            print(form.errors)

    else:
        form = PictureForm()

    return render(request, 'my_files/upload_picture.html', {'form': form})


def validate_file_size(value):
    filesize = value.size
    if filesize > 50_000_000:  # Увеличен максимальный размер для видео
        raise ValidationError('Максимальный размер файла 10Мб')
    return value

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user

            # Загрузка видео в Cloudinary
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Используем request.FILES['path'] для правильного пути к видео
                    resource_type="video",  # Указываем, что загружаемый файл является видео
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME']
                )

                # Сохранение URL видео из Cloudinary в вашу модель
                video.path = upload_result['url']  # Обновите path с URL из Cloudinary
                video.save()

                return redirect('my_files:home')  # Перенаправляем на главную страницу после успешной загрузки

            except Exception as e:
                # Обработка ошибок загрузки
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')

        # Если форма не прошла валидацию
        else:
            print(form.errors)

    else:
        form = VideoForm()

    return render(request, 'my_files/upload_video.html', {'form': form})

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user

            # Загрузка документа в Cloudinary
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Используем request.FILES['path'] для правильного пути к документу
                    resource_type="auto",  # Автоматическое определение типа файла
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME']
                )

                # Сохранение URL документа из Cloudinary в вашу модель
                document.path = upload_result['url']  # Обновите path с URL из Cloudinary
                document.save()

                return redirect('my_files:home')  # Перенаправляем на главную страницу после успешной загрузки

            except Exception as e:
                # Обработка ошибок загрузки
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')

        # Если форма не прошла валидацию
        else:
            print(form.errors)

    else:
        form = DocumentForm()

    return render(request, 'my_files/upload_document.html', {'form': form})


@login_required
def remove_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk, user=request.user)
    if request.method == 'POST':
        picture.delete()
        return redirect('my_files:home')

@login_required
def change_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Используйте имя поля из вашей формы PictureForm
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME']
                )
                picture.path = upload_result['url']
                form.save()
                return redirect('my_files:home')
            except Exception as e:
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')
        else:
            print(form.errors)
    else:
        form = PictureForm(instance=picture)
    return render(request, 'my_files/change_picture.html', {'form': form})


@login_required
def remove_video(request, pk):
    video = get_object_or_404(Video, pk=pk, user=request.user)
    if request.method == 'POST':
        video.delete()
        return redirect('my_files:home')
    # Добавьте здесь дополнительную логику для GET запроса, если необходимо

@login_required
def change_video(request, pk):
    video = get_object_or_404(Video, pk=pk, user=request.user)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Замените 'path' на имя поля из вашей формы
                    resource_type="video",
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME']
                )
                video.path = upload_result['url']
                form.save()
                return redirect('my_files:home')
            except Exception as e:
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')
        else:
            print(form.errors)
    else:
        form = VideoForm(instance=video)
    return render(request, 'my_files/change_video.html', {'form': form})


@login_required
def remove_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    if request.method == 'POST':
        document.delete()
        return redirect('my_files:home')  # После удаления перенаправляем на главную страницу или другую нужную страницу
    return redirect('my_files:home')  # В случае GET запроса также перенаправляем на главную страницу


@login_required
def change_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            try:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['path'],  # Используйте имя поля из вашей формы DocumentForm
                    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
                    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
                    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
                    resource_type="auto"  # Укажите тип ресурса, если он не автоматически определяется
                )
                document.path = upload_result['url']
                form.save()
                return redirect('my_files:home')
            except Exception as e:
                print(f'Ошибка загрузки в Cloudinary: {e}')
                form.add_error(None, 'Ошибка загрузки в Cloudinary. Попробуйте еще раз.')
        else:
            print(form.errors)
    else:
        form = DocumentForm(instance=document)
    
    return render(request, 'my_files/change_document.html', {'form': form})