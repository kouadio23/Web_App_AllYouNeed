from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='allYouNeed-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('food/', views.food, name='allYouNeed-food'),
    path('tourism/', views.tourism, name='allYouNeed-tourism'),
    path('vacation/', views.vacation, name='allYouNeed-vacation'),
    path('entertainment/', views.entertainment, name='allYouNeed-entertainment'),
]

