from django.conf import settings
from django.urls import path, include, re_path
from frontend import views

urlpatterns = [
   path('', views.search, name='search'),
   path('search', views.search, name='search'),
   path('view/<int:pk>', views.IntelView.as_view(), name='view'),
   path('create', views.IntelCreate.as_view(), name='create'),
   path('update/<int:pk>', views.IntelUpdate.as_view(), name='update'),
   path('delete/<int:pk>', views.IntelDelete.as_view(), name='delete'),
   path('bookmark-create', views.BookmarkCreate.as_view(), name='bookmark_create'),
   path('bookmark-add', views.bookmark_add, name='bookmark_add'),

]
