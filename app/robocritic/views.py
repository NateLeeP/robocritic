from django.shortcuts import render, get_object_or_404
from .models import Game, Review


def index(request):
    games = Game.objects.all()
    return render(request, "robocritic/index.html", {"games": games})


def review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = Review.objects.filter(game__id=game_id)
    return render(request, "robocritic/review.html", {"reviews": reviews, "game": game})
