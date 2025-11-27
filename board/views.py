from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["week", "day", "developer"]

    def get_queryset(self):
        qs = super().get_queryset()
        developer = self.request.query_params.get("developer")
        if developer:
            qs = qs.filter(developer=developer)
        return qs
