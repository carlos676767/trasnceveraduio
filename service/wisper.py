from service.Gemini import Gemini
from service.insertResume import InsertResume
import whisper



class Transcriver:
    @staticmethod
    def transcribe():
        model = whisper.load_model("medium")
        result = model.transcribe("audio/audio_baixado.m4a", language="pt")
        text = result["text"]
        ia = Gemini.generate_content(text)
      
        InsertResume.main(ia)
