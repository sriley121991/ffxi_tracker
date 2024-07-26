from django.urls import path
from . import views

app_name = "characters"
urlpatterns = [
    path("", views.characters, name="characters"),
    path("new_character/", views.new_character, name="new_character"),
    path("character/<character_name>/", views.character_detail, name="character_details"),
    path("character/<character_name>/update", views.update_character, name="update_character"),
]