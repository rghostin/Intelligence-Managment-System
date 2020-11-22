from rest_framework import serializers

from intelsAPI.models import Intel, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IntelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Intel
        exclude = ('author',)


