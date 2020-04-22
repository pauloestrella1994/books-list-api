from rest_framework.viewsets import ModelViewSet
from core_list.models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'publication_year', 'edition', 'Authors']

