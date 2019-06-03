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


class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer
    def post(self,request,*args,**kwargs):
        new_category = Category.objects.create(
            name = request.data['name']
        )
        return Response(
            data = CategorySerializer(new_category).data
        )

class CreateApplication(generics.CreateAPIView):
    serializer_class = ApplicationSerializer

    def post(self,request,*args,**kwargs):
        new_application = Application.objects.create(
            name = request.data['name'],
            category = Category.objects.get(id=kwargs['id'])
        )
        return Response(
            data = ApplicationSerializer(new_application).data
        )

class UpdateApplicationById(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def put(self,request,*args,**kwargs):
        get_application = self.queryset.get(id=kwargs['id'])
        serializer = ApplicationSerializer()
        category = Category.objects.get(id=request.data['category'])
        data = {
            'name':request.data['name'],
            'descrition':request.data['descrition'],
            'category':category
        }
        updated_application = serializer.update(get_application,data)
        return Response(ApplicationSerializer(updated_application).data)

class DeleteApplicationById(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def delete(self,request,*args,**kwargs):
        delete_application = self.queryset.get(id=kwargs['id'])
        delete_application.delete()
        return Response(data = {
            'message' : 'Application deleted!'
        })
