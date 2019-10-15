from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("polls/", include("polls.urls")),  # noqa: W291
    path("admin/", admin.site.urls),
]
