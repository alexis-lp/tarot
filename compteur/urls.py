from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('newgame', views.newgame, name='nouvelle partie'),
    path('game/<int:game_id>',views.game, name="accueil de la partie"),
    ]
