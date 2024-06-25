from django.forms import ModelForm, CharField, ImageField, TextInput, FileInput

from django import forms
from .models import MyFile


class MyFileForm(forms.ModelForm):
    class Meta:
        model = MyFile
        fields = ['name', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file.size > 1024 * 1024:  # 1 МБ
            raise forms.ValidationError("Розмір файлу перевищує 1 МБ")
        return file


# class MyFileForm(ModelForm):
#     description = CharField(max_length=300, min_length=5,
#                             widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"}))
#     path = ImageField(widget=FileInput(attrs={"class": "form-control", "id": "formFile", "accept": "file/*"}))
#
#     class Meta:
#         model = MyFile
#         fields = ['description', 'path']
