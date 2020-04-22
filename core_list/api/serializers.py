from rest_framework.serializers import ModelSerializer
from core_list.models import Product
from Authors_list.api.serializers import AuthorsSerializer


class ProductSerializer(ModelSerializer):
    Authors = AuthorsSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'edition', 'publication_year', 'Authors')

    def create_books_list(self, authors, books):
        for author in authors:
            bk = Authors.objects.create(**author)
            Product.authors.add(bk)

    def create(self, validated_data):
        authors = validated_data['Authors']
        del validated_data['Authors']
        books = Product.objects.create(**validated_data)
        self.create_books_list(authors, books)

        return Product