from rest_framework import serializers 
from .models import Project
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):

    stack = TagListSerializerField()

    class Meta:
        model = Project
        fields = ['name','description','repo_link','demo','image', 'stack']