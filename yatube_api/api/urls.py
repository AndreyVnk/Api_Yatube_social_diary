from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path

app_name = 'api'

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token, name='api-token'),
    path('api/v1/', include(router.urls)),
]
