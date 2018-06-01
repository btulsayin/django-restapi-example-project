# Django user ve group modelleri
from django.contrib.auth.models import User, Group
# serializers
from rest_framework import serializers


# UserSerializer adında bir model oluşturduk.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  # db adı
        fields = ('url', 'username', 'email', 'groups')  # db sütünları


# GroupSerializer adında bir model oluşturduk.
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group  # db adı
        fields = ('url', 'name')  # db sütünları