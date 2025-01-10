from rest_framework import viewsets,mixins
from .models import *
from .serializers import *
from rest_framework.exceptions import PermissionDenied

# class PostListSet(mixins.ListModelMixin,viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class = PostSerializer

# class PostUpdateSet(mixins.UpdateModelMixin,viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostUpdateSerializer

#     def perform_update(self, serializer):
#         post=self.get_object()
#         if self.request.user==post.author or self.request.user.is_superuser:
#             serializer.save()
#         else:
#             raise PermissionDenied("Bu postu güncellemeye yetkiniz yok!")
        
# class PostDeleteSet(mixins.DestroyModelMixin,viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

#     def perform_destroy(self, instance):
#         if self.request.user==instance.author or self.request.user.is_superuser:
#             instance.delete()
#         else:
#             raise PermissionDenied("Bu postu silemeye yetkin yok")


class PostViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def perform_update(self, serializer):
        post=self.get_object()
        if self.request.user==post.author or self.request.user.is_superuser:
            serializer.save()
        else:
            raise PermissionDenied("Bu postu güncellemeye yetkiniz yok!")
    def perform_destroy(self, instance):
        if self.request.user==instance.author or self.request.user.is_superuser:
            instance.delete()
        else:
            raise PermissionDenied("Bu postu silemeye yetkin yok")


    

