from django.urls import path

from .api import UserCreateAPI, UserGetObjectAPI, UserYandexAPi, GetCity
from .views import Index

app_name = "index"

urlpatterns = [
    path('index/<str:email>', Index.as_view(), name='index'),
    path('create/', UserCreateAPI.as_view(), name='create_user'),
    path('city/<str:name>', GetCity.as_view(), name='view_city'),
    path('get/<str:email>', UserGetObjectAPI.as_view(), name='get_user'),
    path('view/<str:email>', UserYandexAPi.as_view(), name='view_user'),
]
