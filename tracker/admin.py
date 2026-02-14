from django.contrib import admin
from .models import Course, StudySession


class StudySessionInline(admin.TabularInline):
    model = StudySession
    extra = 0
    fields = ("date", "minutes", "notes")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    inlines = (StudySessionInline,)


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ("course", "date", "minutes", "notes")
    search_fields = ("notes", "course__title")
    list_filter = ("date", "course")
