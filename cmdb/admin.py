from django.contrib import admin
from .models import ServerDetail, Category, Project


@admin.register(ServerDetail)
class ServerDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
