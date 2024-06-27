from django.forms import ModelForm, CharField, ImageField, TextInput, FileInput, FileField
from .models import Picture, Video, Document

class PictureForm(ModelForm):
    description = CharField(
        max_length=300, min_length=5,
        widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"})
    )
    path = ImageField(
        widget=FileInput(attrs={"class": "form-control", "id": "formFile", "accept": "image/*"})
    )

    class Meta:
        model = Picture
        fields = ['description', 'path']


class VideoForm(ModelForm):
    description = CharField(
        max_length=300, min_length=5,
        widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"})
    )
    path = FileField(
        widget=FileInput(attrs={"class": "form-control", "id": "formFile", "accept": "video/*"})
    )

    class Meta:
        model = Video
        fields = ['description', 'path']


class DocumentForm(ModelForm):
    description = CharField(
        max_length=300, min_length=5,
        widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"})
    )
    path = FileField(
        widget=FileInput(attrs={"class": "form-control", "id": "formFile", "accept": "application/*"})
    )

    class Meta:
        model = Document
        fields = ['description', 'path']