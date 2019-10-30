from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse


# Create your views here.


def home(request):
    ids = list(Youtube.objects.all().values_list('music_id', flat=True))
    print(22222222222222,ids)
    return render(request, 'home.html', {'music_ids': ids})


@csrf_exempt
def add_youtube_music(request):
    print("add_youtube_music.............")
    if request.method == 'POST':
        music_id = request.POST.get('music_id')
        print(".................", music_id)
        Youtube.objects.create(music_id=music_id)

        return JsonResponse({})
