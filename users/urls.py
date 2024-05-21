from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("logout/", views.custom_logout, name="logout"),
    path("", include("django.contrib.auth.urls")),
]
