from rest_framework import viewsets, filters
from rest_framework import permissions

from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel, Tag, IntelFile
from intelsAPI.serializers import IntelSerializer, TagSerializer, IntelFileSerializer
from intelsAPI.permissions import IsOwnerOrReadOnly
from rest_framework import generics

from django_filters import rest_framework as dj_filters


class IntelViewSet(viewsets.ModelViewSet):
    queryset = Intel.objects.all().order_by("-last_update")
    serializer_class = IntelSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # search
    filter_backends = [dj_filters.DjangoFilterBackend]
    filterset_class = IntelFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
    #search
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class IntelFileViewSet(viewsets.ModelViewSet):
    queryset = IntelFile.objects.all()
    serializer_class = IntelFileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


