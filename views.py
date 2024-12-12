from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from models import Task
from serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["patch"])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = "completed"
        task.save()
        return Response({"status": "Task marked as completed."})
