from django.urls import path
from .views import index

urlpatterns = [
    path("index", index, name='my_app-index'),
]