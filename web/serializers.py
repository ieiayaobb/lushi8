from rest_framework import serializers

class ChairmanSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=256)
    href = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    img = serializers.CharField(max_length=256)
    num = serializers.CharField(max_length=256)
    type = serializers.CharField(max_length=256)