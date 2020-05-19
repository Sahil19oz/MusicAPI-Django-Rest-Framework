from django.urls import path
from .views import SongList

urlpatterns=[
path("songs/",SongList.as_view(),name="songs-all"),
path("songs/<int:pk>",SongList.as_view()),

]
