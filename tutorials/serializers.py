from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tutorials

class TutorialsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='tutorials-highlight', format='html')
    class Meta:
        model = Tutorials
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tutorials =serializers.HyperlinkedRelatedField(many=True, view_name='tutorials-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tutorials']