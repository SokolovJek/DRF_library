from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet


router = DefaultRouter()
router.register('author', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-path/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
