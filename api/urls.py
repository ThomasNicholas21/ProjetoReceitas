from django.urls import path, include


urlpatterns = [
    path('', include("api.views.model_views.urls")),
    path('', include("api.views.model_views.urls")),
]
