
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('recommendMovies/', views.recommendMovies, name="recommendMovies"),
    path('selectGenre/', views.selectGenre, name="selectGenre")
]