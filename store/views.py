from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from store.models import Collection, Review
from store.serializers import CollectionSerializer, ReviewSerializer

# Create your views here.


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    def get_queryset(self):
         print(self.request.query_params['collection_id'])
         return super().get_queryset()
    
    def perform_destroy(self, instance):
        if instance.products.count()>0:
                return Response(
                "collection has associated products and can not be deleted",
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.delete() # super().perform_destroy


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer