from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from board.views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", include("board.urls")),   # renders board_page -> board.html
]
