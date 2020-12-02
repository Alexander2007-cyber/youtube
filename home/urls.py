from django.urls import path
from .views import home, watch

urlpatterns = [
    path('', home),
    path('watch=<str:code>', watch, name="watch")
]
