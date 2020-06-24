from .models import Project
from rest_framework import viewsets
from .serializers import ProjectSerializer

# Project Info viewset
# allows us to create a CRUD api without specifying methods for functionality

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.filter(show=True)
    serializer_class = ProjectSerializer