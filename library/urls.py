from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, BaseRouter
from authors.views import AuthorModelViewSet
from todo.views import ProjectView, TodoView
from rest_framework.authtoken import views


EXAMPLE = False


router = DefaultRouter()
router.register('author', AuthorModelViewSet)
router.register('projects', ProjectView)
router.register('todo', TodoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-path/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]





if EXAMPLE:
    from mainapp.views import MyFilterModelViewSet, ArticleDjangoFilterViewSet, ArticleModelViewSetFilter, \
        ArticleCustomViewSetFilter, ArticleViewAPI, ArticleRetrieveAPIView, ArticleCreateAPIView, ArticleListAPIView, \
        ArticleDestroyAPIView, ArticleUpdateAPIView, ArticleViewSet, ArticleModelViewSet, ArticleCustomViewSet

    router_second = DefaultRouter()
    router_second.register('view-set', ArticleViewSet, basename='article')
    router_second.register('model-view-set', ArticleModelViewSet, basename='article_model')
    router_second.register('custom-view-set', ArticleCustomViewSet, basename='article_custom_set')

    router_filter = DefaultRouter()
    router_filter.register('param', ArticleModelViewSetFilter, basename='param')
    router_filter.register('filter_django', ArticleDjangoFilterViewSet, basename='param2')
    router_filter.register('filter_my', MyFilterModelViewSet, basename='my_filter')

    urlpatterns.extend([
        path('views/api-view/', ArticleViewAPI.as_view()),
        path('views/generic/list/', ArticleListAPIView.as_view()),
        path('views/generic/create/', ArticleCreateAPIView.as_view()),
        path('views/generic/retrieve/<int:pk>', ArticleRetrieveAPIView.as_view()),
        path('views/generic/destroy/<int:pk>', ArticleDestroyAPIView.as_view()),
        path('views/generic/update/<int:pk>', ArticleUpdateAPIView.as_view()),
        path('views/', include(router_second.urls)),
        path('views/filter/<str:name>', ArticleCustomViewSetFilter.as_view()),
        path('filter/', include(router_filter.urls))
    ])