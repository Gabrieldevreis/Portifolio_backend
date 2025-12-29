from rest_framework import serializers
from .models import Projects,Techs

class TechsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = ['name']


class ProjectsSerializers(serializers.ModelSerializer):
    class Meta: 
        model= Projects
        fields= '__all__'
    techs = TechsSerializer(many=True, read_only=True)