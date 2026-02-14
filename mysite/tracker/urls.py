from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="course_list", permanent=False)),
    path("courses/", views.course_list, name="course_list"),
]
