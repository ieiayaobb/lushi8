from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'username', 'email', 'groups')