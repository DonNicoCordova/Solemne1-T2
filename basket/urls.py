from django.urls import path
from basket import views


urlpatterns = [
    path('', views.player_list, name="player"),
    path('player_list', views.player_list, name="player_list"),
    path('player_add', views.player_add, name="player_add"),
    path('player_edit/<int:pk>/', views.player_edit, name="player_edit"),
    path('player_delete/<int:pk>/', views.player_del, name="player_delete"),
    path('team_list', views.team_list, name="team_list"),
    path('team_add', views.team_add, name="team_add"),
    path('team_edit/<int:pk>/', views.team_edit, name="team_edit"),
    path('team_delete/<int:pk>/', views.team_del, name="team_delete"),
    path('coach_list', views.coach_list, name="coach_list"),
    path('coach_add', views.coach_add, name="coach_add"),
    path('coach_edit/<int:pk>/', views.coach_edit, name="coach_edit"),
    path('coach_delete/<int:pk>/', views.coach_del, name="coach_delete"),
    path('match_list', views.match_list, name="match_list"),
    path('match_delete/<int:pk>/', views.match_del, name="match_delete"),
    path('match_add', views.match_add, name="match_add"),
    path('match_edit/<int:pk>/', views.match_edit, name="match_edit"),
    path('teamcompose_list', views.teamcompose_list, name="teamcompose_list"),
    path('teamcompose_delete/<int:pk>/', views.teamcompose_del, name="teamcompose_delete"),
    path('teamcompose_add', views.teamcompose_add, name="teamcompose_add"),
    path('teamcompose_edit/<int:pk>/', views.teamcompose_edit, name="teamcompose_edit"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
]
