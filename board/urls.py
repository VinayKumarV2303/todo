from django.urls import path
from .views import task_list, update_task_status

urlpatterns = [
    path("api/tasks/", task_list, name="task-list"),
    path("api/tasks/<int:task_id>/status/", update_task_status, name="update-task-status"),
]
