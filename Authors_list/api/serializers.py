from rest_framework.serializers import ModelSerializer
from Authors_list.models import Authors

class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = "__all__"