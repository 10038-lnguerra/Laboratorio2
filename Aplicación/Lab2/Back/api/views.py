from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
from google.cloud import texttospeech
import os
import base64

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("⚠ ERROR: La API Key de Google Gemini no está configurada. Revisa el archivo .env.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def generate_story(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "Error: No se pudo generar el cuento."
    except Exception as e:
        return f"Error al generar el cuento: {str(e)}"

class StoryGeneratorView(APIView):
    def post(self, request):
        prompt = request.data.get("prompt", "").strip()

        if not prompt:
            return Response({"error": "Se requiere un prompt"}, status=status.HTTP_400_BAD_REQUEST)

        story = generate_story(prompt)

        if "Error" in story:
            return Response({"error": story}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"story": story})

GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not GOOGLE_CREDENTIALS:
    raise ValueError("⚠ ERROR: Las credenciales de Google Cloud no están configuradas.")

class TextToSpeechView(APIView):
    def post(self, request):
        text = request.data.get("text", "").strip()
        if not text:
            return Response({"error": "Se requiere un texto"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = texttospeech.TextToSpeechClient()

            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code="es-ES",
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

            response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

            audio_base64 = base64.b64encode(response.audio_content).decode("utf-8")

            return Response({"audio": audio_base64}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Error en TTS: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        