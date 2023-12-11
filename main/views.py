from django.shortcuts import render, get_object_or_404
from .models import Movie


def home(request):
    movies = Movie.objects.all()[:6]
    context = {'movies': movies}
    return render(request, 'main/home.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'main/movie_detail.html', {'movie': movie})
