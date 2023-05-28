from django.http import HttpResponse

from elasticsearch_dsl import Q

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from places.serializers import PlaceSearchSerializer
from .documents import PlaceDocument

class Search(APIView, PageNumberPagination):
    place_serializer = PlaceSearchSerializer
    search_document = PlaceDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'name',
                    'category',
                    'address',
                    'menu',
                    'description',
                ]
            )
        
            search = self.search_document.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.place_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)
