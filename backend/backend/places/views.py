from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .models import Place
import json

def validate_coordinates(coord):
    try:
        float(coord)
    except ValueError:
        raise ValidationError("Invalid coordinate value.")

def validate_coordinates_bound(sw_x, sw_y, ne_x, ne_y):
    if sw_x > ne_x or sw_y > ne_y:
        raise ValidationError("Invalid coordinate bound. Coordinates for SW must be lower than NE.")
   
def place_request(request):
    # Check GET method
    if request.method != 'GET':
        return JsonResponse({"error": "Invalid Request Method"}, status=400)
    
    # Default values
    query = request.GET.get('query', '서울')
    page_num = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('size', 10))
    rect = request.GET.get('rect', None)

    # Filter the Place objects by address
    # place_objects = Place.objects.filter(Q(address__icontains=query))
    place_objects = Place.objects.filter(
        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(address__icontains=query) |
        Q(menu__icontains=query) |
        Q(description__icontains=query)
    )

    # Filter retaurants within the map area
    # Coordinates (x, y) = (longitude, latitude)
    if rect:
        sw_x, sw_y, ne_x, ne_y = rect.split(',')

        validate_coordinates(sw_x)
        validate_coordinates(sw_y)
        validate_coordinates(ne_x)
        validate_coordinates(ne_y)
        validate_coordinates_bound(sw_x, sw_y, ne_x, ne_y)

        place_objects = place_objects.filter(
            Q(coordinates_longitude__gte=sw_x) &
            Q(coordinates_longitude__lte=ne_x) &
            Q(coordinates_latitude__gte=sw_y) &
            Q(coordinates_latitude__lte=ne_y)            
        )

    # Caclulate metadata
    total_count = place_objects.count()
    is_last_page = ((total_count // page_size) + 1) == page_num
    meta = {
        "total_count": total_count, 
        "count": page_size,
        "is_end": is_last_page
    }

    # Retrieve a page of objects from the Place model
    start_index = (page_num - 1) * page_size
    end_index = start_index + page_size
    place_objects = place_objects[start_index : end_index]

    documents = []
    for place in place_objects:
        place_dict = model_to_dict(place)
        place_dict['total_likes'] = place.get_overall_likes() 
        documents.append(place_dict)

    # Build the response
    response_data = {
        'meta': meta,
        'documents': documents,
    }

    return JsonResponse(
        response_data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}, 
        status=200)
