

from service.Downloader import Downloader
from service.wisper import Transcriver
from utils.validations import validacoes
from ui.banner import show_banner

def execScript():

    try:

        show_banner()

        url = validacoes()


        Downloader.download_audio(url)

        Transcriver.transcribe()

    except Exception as e:

        print(e)
 


execScript()