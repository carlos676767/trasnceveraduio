from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class Gemini:
    @staticmethod
    def generate_content(text):
     
        api_key = os.getenv("gemini")
        client = genai.Client(api_key=api_key)

        prompt = (
            "Aja como um roteirista profissional de vídeos. Leia a transcrição abaixo e "
            "transforme-a em um ROTEIRO DE VÍDEO VIRAL para YouTube Shorts ou Reels (deve durar entre 30 a 60 segundos). "
            "O roteiro deve ter um GANCHO FORTE nos primeiros 3 segundos, ser direto ao ponto e ter frases curtas e dinâmicas.\n"
            "Corrija qualquer erro de português na fala e entregue um texto formatado pronto para ser lido ou usado em voz sintética "
            "(sem emojis excessivos ou formatações markdown que atrapalhem o áudio). "
            f"Segue abaixo a transcrição na íntegra:\n\n{text}"
        )
        response = client.models.generate_content(
            model="gemini-3-flash-preview",contents = prompt
        )
        
        return (response.text)