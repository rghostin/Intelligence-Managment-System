from rest_framework import viewsets

from intelsAPI.models import Intel, Tag
from intelsAPI.serializers import IntelSerializer, TagSerializer


class IntelViewSet(viewsets.ModelViewSet):
    queryset = Intel.objects.all().order_by("last_update")
    serializer_class = IntelSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer