from django.shortcuts import render, get_object_or_404
from .models import Game, Review
from datetime import date, timedelta, datetime


def index(request):
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        games = Game.objects.filter(title__istartswith=search_query)
    else:
        print("Get Request")
        cutoff_date = datetime.now() - timedelta(days=70)
        games = Game.objects.filter(release_date__gte=cutoff_date.date())

    return render(request, "robocritic/index.html", {"games": games})


def review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = Review.objects.filter(game__id=game_id)
    return render(request, "robocritic/review.html", {"reviews": reviews, "game": game})


def search(request):
    print(request.GET)
    return render(request, "robocritic/search_bar.html")
