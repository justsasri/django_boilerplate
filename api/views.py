from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from app.models import Category

from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.select_related("parent").all()
    filter_backends = [SearchFilter, OrderingFilter]
    serializer_class = CategorySerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name"]
