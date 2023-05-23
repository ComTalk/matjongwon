from django.urls import path
from .views import KakaoAuthorizeView
from .views import KakaoCallBackView
from .views import KakaoUserInfoView


urlpatterns = [
    path('kakao/authorize/', KakaoAuthorizeView.as_view()),
    path('kakao/callback/', KakaoCallBackView.as_view()),
    path('kakao/userinfo/', KakaoUserInfoView.as_view()),
]
