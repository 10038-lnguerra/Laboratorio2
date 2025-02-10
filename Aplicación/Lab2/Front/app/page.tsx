"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [audio, setAudio] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingAudio, setLoadingAudio] = useState(false);

  // Función para generar el cuento
  const generateStory = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${process.env.BACKEND_URL}/api/generate/`, {
        prompt,
      });
      setStory(response.data.story);
      setAudio(null);
    } catch (error) {
      console.error("Error al generar la historia:", error);
    }
    setLoading(false);
  };

  // Función para convertir en voz 
  const convertToSpeech = async () => {
    if (!story) return;
    
    setLoadingAudio(true);
    try {
      const response = await axios.post(`${process.env.BACKEND_URL}/api/tts/`, {
        text: story,
      });
      setAudio(`data:audio/mp3;base64,${response.data.audio}`);
    } catch (error) {
      console.error("Error al convertir texto a voz:", error);
    }
    setLoadingAudio(false);
  };

  // Función para reproducir el audio
  const playAudio = () => {
    if (audio) {
      const audioElement = new Audio(audio);
      audioElement.play();
    }
  };

  return (
    <div className="flex flex-col items-center p-6 bg-blue-500 text-white min-h-screen">
      <h1 className="text-4xl font-bold mb-6">📖 Generador de Cuentos</h1>
      
      <label htmlFor="storyText" className="text-lg mb-2">Ingresa un tema para tu cuento:</label>
      <textarea
        id="storyText"
        className="border border-blue-300 rounded-lg p-3 mb-4 w-full max-w-xl h-32 text-gray-900"
        placeholder="Escribe tu tema aquí..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        className="bg-blue-700 hover:bg-blue-600 text-white p-3 rounded-lg mb-4 w-full max-w-xl"
        onClick={generateStory}
        disabled={loading}
      >
        {loading ? "Generando..." : "Generar Cuento"}
      </button>

      {story && (
        <div className="bg-blue-600 p-4 rounded-lg w-full max-w-xl text-white shadow-lg">
          <p className="text-lg text-blue-200 mb-4">{story}</p>

          <div className="flex space-x-4">
            <button
              className="bg-blue-900 hover:bg-blue-800 text-white p-3 rounded-lg w-full"
              onClick={convertToSpeech}
              disabled={loadingAudio}
            >
              {loadingAudio ? "Generando Audio..." : "Convertir a Audio 🎧"}
            </button>

            {audio && (
              <button
                className="bg-white text-blue-900 hover:bg-zinc-200 p-3 rounded-lg w-full"
                onClick={playAudio}
              >
                Reproducir Audio ▶️
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
