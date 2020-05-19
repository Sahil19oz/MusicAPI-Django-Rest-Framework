from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer

class SongList(generics.ListCreateAPIView):
    queryset=Songs.objects.all()
    serializer_class=SongSerializer
