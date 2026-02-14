from django.shortcuts import render

from .models import Course


def course_list(request):
    """Public page listing all courses."""
    courses = Course.objects.all().order_by("title")
    return render(request, "tracker/course_list.html", {"courses": courses})
