from django.urls import path
from .views import RegistrationAPIView, ConfirmUserAPIView, AuthorizationAPIView
urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
    path('login/', AuthorizationAPIView.as_view()),
]