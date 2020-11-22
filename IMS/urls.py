from django.contrib import admin
from django.urls import path, include
import intelsAPI.views as intelsAPI_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'intels', intelsAPI_views.IntelViewSet)
router.register(r'tags', intelsAPI_views.TagsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
