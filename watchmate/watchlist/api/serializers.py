from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    id = serializers.UUIDField(read_only=True)
