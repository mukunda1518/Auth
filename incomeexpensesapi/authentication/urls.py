from django.urls import path
from .views import RegistrationView, VerifyEmail

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
]