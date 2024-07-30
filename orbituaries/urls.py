from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('submit_orbituary/', views.SubmitOrbituary, name='submitOrbituary'),
    path('view_orbituaries/', views.ViewOrbituaries, name='viewOrbituaries'),
]
