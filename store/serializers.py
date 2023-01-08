from rest_framework import serializers

from store.models import Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
    
    def get_product_count(self, collection):
        return collection.products.count()
    

class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='product-detail'
    )
    class Meta:
        model = Review
        fields = ['id', 'product','name', 'date', 'description']