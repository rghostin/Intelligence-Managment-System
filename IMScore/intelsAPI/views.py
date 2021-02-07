from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from intelsAPI.bookmarker import Bookmarker
from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel, Tag, IntelFile
from intelsAPI.serializers import IntelSerializer, TagSerializer, IntelFileSerializer
from intelsAPI.permissions import IsOwnerOrReadOnly

from django_filters import rest_framework as dj_filters


def assert_intel_author(intel, user):
    if intel.author != user:
        raise PermissionDenied


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
    permission_classes = (permissions.IsAuthenticated,)

    def check_permissions(self, request):
        intel_id = request.data.get('intel')
        if intel_id:
            intel = get_object_or_404(Intel, pk=intel_id)
            assert_intel_author(intel, request.user)
        return super().check_permissions(request)


class BookmarkAdd(APIView):
    def post(self, request, format=None):
        intel_id = request.data.get('intel_id')
        link = request.data.get('link')
        filename = request.data.get('filename', None)
        if filename == '':
            filename = None

        intel = get_object_or_404(Intel, pk=intel_id)
        assert_intel_author(intel=intel, user=request.user)

        try:
            intelfile = Bookmarker.create_snapshot(intel=intel, link=link, filename=filename)
        except Exception as e:
            raise APIException("Unable to create snapshot")
        else:
            intelfileSerializer = IntelFileSerializer(intelfile)
            return Response(intelfileSerializer.data)
