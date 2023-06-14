from pytube import YouTube
from pydub import AudioSegment
import os

prompt = input('Deja aquí el enlace de YouTube que se va a descargar -->')

def Download(URL):    
    try:
        output_format = input('Ingrese la extensión de salida deseada (por ejemplo, mp3, wav, Flac): ')
        video = YouTube(URL)
        downloadvid = video.streams.filter(only_audio=True).first()
        vid = downloadvid.download()
        audio = AudioSegment.from_file(vid)
        audio.export(f'{video.title}.{output_format}', format=output_format)
        print(f"La descarga se completó exitosamente. El archivo '{video.title}.{output_format}' se ha guardado.")
        os.remove(vid)
    except:
        print("Ha ocurrido un error durante la descarga.")

Download(prompt)