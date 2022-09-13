from django.urls import path, include

from watchlist_app.models import Review
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', views.StreamPlatformVs, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchListDetailAV.as_view(), name = 'movie-details'),
    path('', include(router.urls)),
    # path('stream/',views.StreamPlatformListAV.as_view(), name='stream'),
    # path('stream/<int:pk>',views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    # path('review/',views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>',views.ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create', views.ReviewCreate.as_view(), name='review-create'), #all the reviews for the particular movie
    path('<int:pk>/review', views.ReviewList.as_view(), name='review-list'), #all the reviews for the particular movie
    path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'), #detail of a speicifc review
]
