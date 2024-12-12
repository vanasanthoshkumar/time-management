from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
]
