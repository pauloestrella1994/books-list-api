from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from csv_reader.models import Authors

class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = "__all__"