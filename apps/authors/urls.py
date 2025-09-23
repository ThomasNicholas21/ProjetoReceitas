from django.urls import path
from apps.authors import views


urlpatterns = [
    path("register/", views.register_view, name="register")
]
