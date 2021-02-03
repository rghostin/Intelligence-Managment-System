from django.urls import path, include
from rest_framework import routers

import intelsAPI.views as intelsAPI_views

router = routers.DefaultRouter()
router.register(r'intels', intelsAPI_views.IntelViewSet, basename='intels')
router.register(r'tags', intelsAPI_views.TagsViewSet)
router.register(r'intelfiles', intelsAPI_views.IntelFileViewSet, basename='intelfiles')

urlpatterns = [
    path('', include(router.urls)),
    path('bookmark-add', intelsAPI_views.BookmarkAdd.as_view(), name='bookmark_add'),
]
