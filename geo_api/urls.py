from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("geo_core.urls")),
    path("admin/", admin.site.urls),
]