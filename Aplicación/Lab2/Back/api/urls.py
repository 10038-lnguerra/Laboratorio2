from django.urls import path
from .views import StoryGeneratorView
from .views import TextToSpeechView

urlpatterns = [
    path('generate/', StoryGeneratorView.as_view(), name='generate-story'),
    path('tts/', TextToSpeechView.as_view(), name='text-to-speech'),
]