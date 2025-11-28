from django.urls import path
from .views import board_page

urlpatterns = [
    path("", board_page, name="board"),
]
