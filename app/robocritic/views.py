from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Game
def index(request):
    games = Game.objects.all()

    return render(request, 'robocritic/index.html', {'games': games})

