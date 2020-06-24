from rest_framework import serializers
from .models import Project

# project serializer
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['name','description','repo_link','demo','image']