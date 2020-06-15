from rest_framework import serializers
from tutorials.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'highlighted', 'owner_id', 'title', 'code', 'created', 'description','updated', 'Image', 'description']


# class UserSerializer(serializers.ModelSerializer):
#     tutorials =serializers.HyperlinkedRelatedField(many=True, view_name='tutorial-detail', read_only=True)
    
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'tutorials']