from django.urls import path
from .views import test_view


app_name = 'recipe'


urlpatterns = [
    path('test/', test_view())
]
