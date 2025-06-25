from django.urls import path
from recipes import views


app_name = 'recipe'


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id_recipe>/', views.recipe)
]
