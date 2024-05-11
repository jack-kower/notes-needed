from django.urls import path
from .views import NoteViewSet


urlpatterns = [
    path('note/', NoteViewSet.as_view({'post': 'create'})),
]
