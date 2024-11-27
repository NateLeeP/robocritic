from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("review/<int:game_id>/", views.review, name="review"),
    path("search", views.search, name="search"),
]
