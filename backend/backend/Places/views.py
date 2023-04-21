from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q
from django.core.exceptions import ValidationError

from .models import Place
import json

def validate_coordinates(coord):
    try:
        float(coord)
    except ValueError:
        raise ValidationError("Invalid coordinate value.")
    
def placeRequest(request):
    # Initialize params
    
    if request.method != 'GET':
        return JsonResponse({"error": "Invalid Request Method"}, status=400)
    
    query = request.GET.get('query', '강남구')
    page_num = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('size', 10))
    rect = request.GET.get('rect', None)

    # Filer the Place objects by address
    place_objects = Place.objects.filter(Q(address__icontains=query))

    # filter retaurants within the map area
    if rect:
        ma

    # Caclulate metadata
    total_count = place_objects.count()
    isLastPage = ((total_count // page_size) + 1) == page_num
    meta = {
        "total_count": total_count, 
        "count": page_size,
        "is_end": isLastPage
    }

    # Retrieve a page of objects from the Place model
    start_index = (page_num - 1) * page_size
    end_index = start_index + page_size
    place_objects = place_objects[start_index : end_index]
    documents = list(place_objects.values())

    # Build the response
    response_data = {
        'meta': meta,
        'documents': documents,
    }

    return JsonResponse(response_data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}, 
        status=200)
