from django.urls import path
from api.api import GetCategoryList , GetCategoryById,GetApplicationList, GetApplicationById,GetApplicationByCategoryId


urlpatterns = [
    path('GetCategoryList/',GetCategoryList.as_view()),
    path('GetCategoryById/<int:id>/',GetCategoryById.as_view()),
    path('GetApplicationList/',GetApplicationList.as_view()),
    path('GetApplicationByCategoryId/<int:id>/',GetApplicationByCategoryId.as_view()),
]