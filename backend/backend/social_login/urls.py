from django.urls import path
from .views import KakaoCallBackView


urlpatterns = [
    path('kakao_callback/', KakaoCallBackView.as_view()),
]
