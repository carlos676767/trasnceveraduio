import whisper
import yt_dlp
from google import genai
import os
from dotenv import load_dotenv
import re
import json
load_dotenv()


class Downloader:
    @staticmethod
    def download_audio(url):
        ydl_opts = {
            'format': 'm4a/bestaudio/best', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
            'outtmpl': 'audio_baixado.m4a', 
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download concluído: audio_baixado.m4a")


class Gemini:
    @staticmethod
    def generate_content(text):
     
        api_key = os.getenv("gemini")
        client = genai.Client(api_key=api_key)

        prompt= "pegue essa transcrição e faca um resumo dela e na outra parte tire os erros de portugues retornando em um arquivo txt formatado segue abaixo o texto " + text
        response = client.models.generate_content(
            model="gemini-3-flash-preview",contents = prompt
        )
        
        return (response.text)


class RemoveJsonName:
   @staticmethod
   def main(text):
     
      text = text.replace('```json', '').replace('```', '')
      return text.strip()

class JsoInsert:
   @staticmethod
   def main(text):
    file_path = 'transcrebe.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Arquivo {file_path} salvo e formatado com sucesso!")


class Transcriver:
    @staticmethod
    def transcribe():
        model = whisper.load_model("medium")
        result = model.transcribe("audio_baixado.m4a", language="pt")
        text = result["text"]
        ia = Gemini.generate_content(text)
        # resultIa =  RemoveJsonName.main(ia)
        JsoInsert.main(ia)




Downloader.download_audio("https://www.instagram.com/reel/DUG0LhyEqo8/?igsh=MTkydnBhenc0b2s4Zw==")
Transcriver.transcribe()
