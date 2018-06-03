from django.urls import path
from basket import views


urlpatterns = [
    path('', views.player_list, name="player"),
    path('player_list', views.player_list, name="player_list"),
    path('player_add', views.player_add, name="player_add"),
    path('player_edit/<int:pk>/', views.player_edit, name="player_edit"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
]
