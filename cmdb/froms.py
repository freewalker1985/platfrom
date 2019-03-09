from .models import ServerDetail, Project, Category
from django import forms


class ServerDetailForm(forms.ModelForm):
    model = ServerDetail


class ProjectForm(forms.ModelForm):
    model = Project


class CategoryForm(forms.ModelForm):
    model = Category
