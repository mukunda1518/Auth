from django.urls import path
from .views import RegistrationView, VerifyEmail, LoginAPIView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]