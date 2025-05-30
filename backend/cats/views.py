"""
ViewSets for the cats application.

This module defines the API endpoints for managing Cat and Achievement objects.
- CatViewSet: Provides CRUD operations for Cat instances, with pagination and
automatic owner assignment on creation.
- AchievementViewSet: Provides CRUD operations for Achievement instances
without pagination.
"""


from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Cat objects.

    On creation, the owner field is automatically set to the current user.
    """

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        """Save a new Cat instance with the current user as the owner."""
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Achievement objects.

    Pagination is disabled for this endpoint.
    """

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
