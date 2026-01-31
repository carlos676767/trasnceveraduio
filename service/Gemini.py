from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

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