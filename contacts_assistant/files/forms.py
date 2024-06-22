from django.forms import ModelForm, CharField, ImageField, TextInput, FileInput

from .models import MyFile


class MyFileForm(ModelForm):
    description = CharField(max_length=300, min_length=5,
                            widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"}))
    path = ImageField(widget=FileInput(attrs={"class": "form-control", "id": "formFile", "accept": "file/*"}))

    class Meta:
        model = MyFile
        fields = ['description', 'path']
