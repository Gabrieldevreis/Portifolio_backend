from django.shortcuts import render
from .serializers import ProjectsSerializers
from rest_framework.viewsets import ModelViewSet
from .models import Projects

# Create your views here.

class ProjectView(ModelViewSet):
    queryset= Projects.objects.all()
    serializer_class = ProjectsSerializers