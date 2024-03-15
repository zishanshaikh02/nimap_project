
from rest_framework import serializers
from .models import Client, Project



class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    
    

    

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name','users']

    def get_client_name(self, obj):
        return obj.client.client_name
    


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = ProjectSerializer(many=True, read_only=True)




    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_by', 'created_at']

