# speech_to_text.py
import speech_recognition as sr

def perform_recognition(filename) -> str:
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.listen(source)

    return r.recognize_google(audio)