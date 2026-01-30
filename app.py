import whisper


class Transcriver:
    @staticmethod
    def transcribe():
        model = whisper.load_model("medium")
        result = model.transcribe("videoplayback (4).m4a", language="pt")
        text = result["text"]

