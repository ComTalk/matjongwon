import requests
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect


class KakaoAuthorizeView(View):
     def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "http://localhost:8000/oauth/kakao/callback"
        client_id = "c5d2f854b236f050858192c2763f47f7"
        uri = f'{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}'
        return redirect(uri)


class KakaoCallBackView(View):
    def get(self, request):
        print("KakaoCallBackView")
        print(request.GET["code"])
        data = {
            "grant_type" : "authorization_code",
            "client_id" : "c5d2f854b236f050858192c2763f47f7",
            "redirect_uri" : "http://localhost:8000/oauth/kakao/callback",
            "code" : request.GET["code"],   
        }
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api, data=data).json()["access_token"]
        print("access_token:", access_token)
        return redirect(f'http://localhost:8000/oauth/kakao/userinfo?access_token={access_token}')
        # return JsonResponse(data)

class KakaoUserInfoView(View):
    def to_string(self, kwargs):
        return '&'.join([f'{k}={v}' for k,v in kwargs.items()])
    def get(self, request):
        access_token = request.GET["access_token"],
        kakao_user_api = "https://kapi.kakao.com/v2/user/me"
        headers = {"Authorization" : f"Bearer ${access_token}"}
        response = requests.get(kakao_user_api, headers=headers).json()
        user_info = dict()
        user_info['user_id'] = 'k_' + str(response['id'])
        user_info['nickname'] = response['properties']['nickname']
        user_info['profile_image'] = response['properties']['profile_image']
        user_info['email'] = response['kakao_account']['email']
        user_info['age_range'] = response['kakao_account']['age_range']
        user_info['birthday'] = response['kakao_account']['birthday']
        user_info['access_token'] = access_token
        return redirect(f'http://localhost:8080/oauth/kakao/userinfo?{self.to_string(user_info)}')
