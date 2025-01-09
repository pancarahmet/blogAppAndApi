from django.urls import path,include
from .views import *


urlpatterns=[
    path('post-list/',PostListView.as_view(),name="postList"),
    path('<int:pk>/',PostDetailView.as_view(),name="postDetay"),
    path('create-post/',PostCreateView.as_view(),name="postCreate"),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='postUpdate'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='postDelete'),
]