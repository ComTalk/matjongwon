from rest_framework import pagination

class PlacePagination(pagination.PageNumberPagination):
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'meta': {

            }
            ('meta', self.page.paginator.count),
            ('results', data)
        })
