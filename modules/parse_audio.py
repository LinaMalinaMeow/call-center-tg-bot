import os
from modules.env import env
import subprocess
import speech_recognition as sr
import requests

def audio_to_text(dest_name: str):
    r = sr.Recognizer()

    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="ru_RU")
    return result

def parse_audio(file_info):
    try:
        path = file_info.file_path
        fname = os.path.basename(path)
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(env.get('TG_API_KEY'), file_info.file_path))
        with open(fname+'.oga', 'wb') as f:
            f.write(doc.content)
        subprocess.run(['ffmpeg', '-i', fname+'.oga', fname+'.wav'])
        result = format(audio_to_text(fname+'.wav'))
        return result
    except:
        return False
    finally:
        os.remove(fname+'.wav')
        os.remove(fname+'.oga')