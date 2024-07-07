from django.urls import path, include
from .views import authView, home
from . import views


urlpatterns = [
    path("", home, name="home"),
    path('reserve/<int:amenity_id>/', views.create_reservation, name='create_reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]