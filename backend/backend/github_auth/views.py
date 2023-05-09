import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests


@csrf_exempt
def github_token_exchange(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        client_id = data.get('clientId')
        client_secret = data.get('clientSecret')
        redirect_uri = data.get('redirectUri')

        response = requests.post(
            'https://github.com/login/oauth/access_token',
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'code': code,
                'redirect_uri': redirect_uri,
            },
            headers={'Accept': 'application/json'},
        )

        return JsonResponse(response.json())

    return JsonResponse({'error': 'Invalid request method'}, status=405)
