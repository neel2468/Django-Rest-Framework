from django.urls import path
from api.api import (GetCategoryList , GetCategoryById,GetApplicationList, 
GetApplicationById,GetApplicationByCategoryId,CreateCategory,CreateApplication,UpdateApplicationById,DeleteApplicationById)


urlpatterns = [
    path('GetCategoryList/',GetCategoryList.as_view()),
    path('GetCategoryById/<int:id>/',GetCategoryById.as_view()),
    path('GetApplicationList/',GetApplicationList.as_view()),
    path('GetApplicationByCategoryId/<int:id>/',GetApplicationByCategoryId.as_view()),
    path('CreateCategory/',CreateCategory.as_view()),
    path('CreateApplication/<int:id>',CreateApplication.as_view()),
    path('UpdateApplicationById/<int:id>',UpdateApplicationById.as_view()),
    path('DeleteApplicationById/<int:id>',DeleteApplicationById.as_view()),
]