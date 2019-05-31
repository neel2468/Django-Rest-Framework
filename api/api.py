from rest_framework import generics
from api.models import Category,Application
from api.serializers import CategorySerializer,ApplicationSerializer
from rest_framework.response import Response
from rest_framework.views import status

class GetCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GetCategoryById(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request,*args,**kwargs):
        try:
            category = self.queryset.get(id=kwargs['id'])
            return Response(CategorySerializer(category).data)
        except Category.DoesNotExist:
            return Response(
                 data={
                    "message": "Category with id: {} does not exist".format(kwargs['id'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class GetApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
class GetApplicationById(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = CategorySerializer

    def get(self,request,*args,**kwargs):
        try:
            category = self.queryset.get(id=kwargs['id'])
            return Response(ApplicationSerializer(category).data)
        except Application.DoesNotExist:
            return Response(
                 data={
                    "message": "Application with id: {} does not exist".format(kwargs['id'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class GetApplicationByCategoryId(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get(self,request,*args,**kwargs):
        try:
            application =  Application.objects.filter(category=kwargs['id'])
            return Response(ApplicationSerializer(application,many=True).data)
        except Application.DoesNotExist:
            return Response(
                    data={
                    "message": "Application with id: {} does not exist".format(kwargs['id'])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
#    def get(self,request,id):
#        application = Application.objects.filter(category=id)
#        return Response(ApplicationSerializer(application,many=True).data)     