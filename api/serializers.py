from rest_framework import serializers
from api.models import Category,Application

class CategorySerializer(serializers.ModelSerializer):
    applications = serializers.SerializerMethodField('get_category_application')
    class Meta:
        model = Category
        fields = ('name','applications')
    
    def get_category_application(self,obj):

        applications = Application.objects.filter(category=obj)
        return ApplicationSerializer(applications,many=True).data
 

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
