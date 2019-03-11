from .models import ServerDetail, Project, Category
from django import forms


class ServerDetailForm(forms.ModelForm):
    class Meta:
        model = ServerDetail
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
