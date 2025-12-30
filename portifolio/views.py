from rest_framework.viewsets import ModelViewSet
from .models import Projects, Profile, Certificate, Experience
from .serializers import (
    ProjectsSerializers,
    ProfileSerializers,
    CertificateSerializers,
    ExperienceSerializers,
)


class ProjectView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializers


class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class CertificateView(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers


class ExperienceView(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers
