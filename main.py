from pytube import YouTube
from pydub import AudioSegment

prompt = input('Deja aquí el enlace de YouTube que se va a descargar -->')

def Download(URL):    
    try:
        video = YouTube(URL)
        downloadvid = video.streams.filter(only_audio=True).first()
        vid = downloadvid.download()
        audio = AudioSegment.from_file(vid)
        audio.export(f'{}.mp3', format='mp3')
        print("La descarga se completó exitosamente.")
    except:
        print("Ha ocurrido un error durante la descarga.")

Download(prompt)

