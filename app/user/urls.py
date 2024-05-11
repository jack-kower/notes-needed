from django.urls import path, include
from .views import UserCreateView

urlpatterns = [
    path('auth/users/', UserCreateView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
