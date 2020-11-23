from rest_framework import serializers

from intelsAPI.models import Intel, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IntelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Intel
        fields = '__all__'
        # exclude = ('author',)


