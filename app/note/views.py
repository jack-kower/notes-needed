from rest_framework import serializers
from core.models import Note
from .serializers import NoteSerializer
from  rest_framework import viewsets
from rest_framework import permissions


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
