from rest_framework import serializers

from intelsAPI.models import Intel, Tag, IntelFile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IntelSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())

    class Meta:
        model = Intel
        fields = '__all__'


class IntelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntelFile
        fields = '__all__'

