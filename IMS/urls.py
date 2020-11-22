from django.contrib import admin
from django.urls import path, include
import intelsAPI.views as intelsAPI_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'intels', intelsAPI_views.IntelViewSet)
router.register(r'tags', intelsAPI_views.TagsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
