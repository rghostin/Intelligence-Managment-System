from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import intelsAPI.views as intelsAPI_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'intels', intelsAPI_views.IntelViewSet, basename="intels")
router.register(r'tags', intelsAPI_views.TagsViewSet)

urlpatterns = [
    path('', include('frontend.urls')),

    path('auth/', include('django.contrib.auth.urls')),

    path('api/', include('intelsAPI.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # production: rm
