from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at'] #de mas nuevo a mas viejo, sin el -, ordena de mas viejo a mas nuevo
    filterset_fields = ['post'] #http://127.0.1:8000/api/comments/?post={id}
