from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/full', views.PostFullView.as_view(), name='post_full'),
    path('alternative/', views.PostListAlternativeView.as_view(), name='post_list_alternative'),
]