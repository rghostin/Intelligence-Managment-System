from rest_framework import serializers

from intelsAPI.models import Intel, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class IntelSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Intel
        fields = '__all__'


