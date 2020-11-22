from rest_framework import viewsets, filters
from rest_framework import permissions

from intelsAPI.models import Intel, Tag
from intelsAPI.serializers import IntelSerializer, TagSerializer
from intelsAPI.permissions import IsOwnerOrReadOnly


class IntelViewSet(viewsets.ModelViewSet):
    search_fields = ['title',]
    filter_backends = [filters.SearchFilter,]
    queryset = Intel.objects.all().order_by("last_update")
    serializer_class = IntelSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
