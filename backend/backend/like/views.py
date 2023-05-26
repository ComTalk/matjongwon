from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from users.models import User
from places.models import Place
from .models import Like, DisLike
from django.views.decorators.csrf import csrf_exempt
from .utils import *

def retrieve_data(request):
    user_id = request.POST.get('user_id')
    user = get_object_or_404(User, pk=user_id)

    place_id = request.POST.get('place_id')
    place = get_object_or_404(Place, pk=place_id)

    try:
        place.likes
    except Place.likes.RelatedObjectDoesNotExist as identifier:
        Like.objects.create(place=place)

    try:
        place.dislikes
    except Place.dislikes.RelatedObjectDoesNotExist as identifier:
        DisLike.objects.create(place=place)
    
    return user, place

@csrf_exempt
@require_POST
def like_button(request):
    user, place = retrieve_data(request)

    if place.likes.users.filter(pk=user.pk).exists():
        place.likes.users.remove(user)
        remove_liked(user.pk,place.pk) 
        is_liked = 0
    elif place.dislikes.users.filter(pk=user.pk).exists():
        place.dislikes.users.remove(user)
        place.likes.users.add(user)
        is_liked = 1
        update_liked(user.pk,place.pk, is_liked) 
    else:
        place.likes.users.add(user)
        is_liked = 1
        place_data = {
            "restaurant_id": str(place.pk),
            "restaurant_name": place.name,
            "location": {
                "city": "Seoul",
                "country": "South Korea"
            },
            "category": place.category,
            "rating": is_liked,
        }
        create_liked(user.pk, place_data)

    total_likes = place.get_overall_likes()

    response = {
        'is_liked': is_liked,
        'total_likes': total_likes,
    }

    return JsonResponse(response)

@csrf_exempt
@require_POST
def dislike_button(request):
    user, place = retrieve_data(request)

    if place.dislikes.users.filter(pk=user.pk).exists():
        place.dislikes.users.remove(user)
        remove_liked(user.pk,place.pk) 
        is_liked = 0
    elif place.likes.users.filter(pk=user.pk).exists():
        place.likes.users.remove(user)
        place.dislikes.users.add(user)
        is_liked = -1
        update_liked(user.pk,place.pk, is_liked) 
    else:
        place.dislikes.users.add(user)
        is_liked = -1
        place_data = {
            "restaurant_id": str(place.pk),
            "restaurant_name": place.name,
            "location": {
                "city": "Seoul",
                "country": "South Korea"
            },
            "category": place.category,
            "rating": is_liked
        }
        create_liked(user.pk, place_data)

    total_likes = place.get_overall_likes()

    response = {
        'is_liked': is_liked,
        'total_likes': total_likes,
    }

    return JsonResponse(response)
