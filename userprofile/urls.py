from django.urls import path
from .views import CustomAuthToken, RegisterView, UserDataCreateAPIView, UserDataUpdateListAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/',CustomAuthToken.as_view()),
    path('userdata/', UserDataCreateAPIView.as_view()),
    path('userdata/<int:pk>', UserDataUpdateListAPIView.as_view()),
]
