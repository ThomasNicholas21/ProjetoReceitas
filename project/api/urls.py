from django.urls import path, include


urlpatterns = [
    path('', include("project.api.views.model_views.urls")),
    path('', include("project.api.views.user_views.urls")),
]
