from rest_framework import serializers
from .models import (
    Projects, Techs, Profile,
    Certificate, Activity, Experience
)


class TechsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = '__all__'


class ProjectsSerializers(serializers.ModelSerializer):
    techs = TechsSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ExperienceSerializers(serializers.ModelSerializer):
    atividades = ActivitySerializers(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'
