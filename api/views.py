from rest_framework import generics
from api.models import Category,Application
from api.serializers import CategorySerializer,ApplicationSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
