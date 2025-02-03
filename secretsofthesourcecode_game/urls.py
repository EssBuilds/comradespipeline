from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('accuse/', views.make_accusation, name='make_accusation'),
    path('lose/', views.lose, name='lose'),
]