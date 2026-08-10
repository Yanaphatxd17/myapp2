from django.contrib import admin
from .models import Student, Major


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "st_id",
        "prefix_name",
        "fname",
        "lname",
        "major",
    )


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('mj_name',)
