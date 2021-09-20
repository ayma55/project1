
from .views import RegisterView,VerifyEmail
from django.urls import path

urlpatterns = [
path('register/', RegisterView.as_view(), name='register'),
path('email-verify/', RegisterView.as_view(), name='email-verify'),
]
