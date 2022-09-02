from django.urls import path

from watchlist_app.models import Review
from . import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name = 'movie-details'),
    path('stream/',views.StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>',views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('stream/<int:pk>/review', views.ReviewList.as_view(), name='stream-detail'),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
]
