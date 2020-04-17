from rest_framework.viewsets import ModelViewSet
from csv_reader.models import Authors
from .serializers import AuthorsSerializer

class AuthorsViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filterset_fields = '__all__'

