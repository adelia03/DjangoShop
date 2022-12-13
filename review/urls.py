from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, CreateRatingAPIview

router = DefaultRouter()
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rating/', CreateRatingAPIview.as_view())
]