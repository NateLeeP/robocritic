from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Game, Review
def index(request):
    games = Game.objects.all()

    return render(request, 'robocritic/index.html', {'games': games})

def review(request, game_id):
    reviews = Review.objects.filter(game__id=game_id)
    return render(request, 'robocritic/review.html', {'reviews': reviews})

