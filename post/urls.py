from django.urls import path, include
from .views import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<post_id>/', views.post, name='post_detail'),
    path('createPost/', views.create_post, name='create_post'),
]
