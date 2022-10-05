from django.urls import path

from constructor.views import PageObjectAPI

app_name = "constructor"

urlpatterns = [
    path('pages', PageObjectAPI.as_view(), name='pages'),
]