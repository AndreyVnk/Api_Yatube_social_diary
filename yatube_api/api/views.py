from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)
from .permissions import IsOwner
from posts.models import Comment, Group, Post, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        post_id = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post, id=post_id))
