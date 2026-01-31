import yt_dlp

class Downloader:
    @staticmethod
    def download_audio(url):
        ydl_opts = {
            'format': 'm4a/bestaudio/best', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
            'outtmpl': 'audio/audio_baixado.m4a', 
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download concluído: audio/audio_baixado.m4a")