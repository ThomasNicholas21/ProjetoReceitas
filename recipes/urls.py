from django.urls import path
from recipes import views


app_name = 'recipes'


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id_recipe>/', views.recipe, name='recipe')
]
