from rest_framework import serializers 

from watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['created', 'updated']

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        exclude = ['created']
        read_only_fields = ['id']

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        exclude = ['created']
        read_only_fields = ['id']



'''
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')
    return value

class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField(required=False)
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description should not equals')
        return data
'''