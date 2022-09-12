import pyaudio
import wave
import speech_recognition as sr

def record(seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = seconds
    PAUSE_SECONDS = 2
    WAVE_OUTPUT_FILENAME = "output.wav"
    MAX_PAUSE = int(RATE / CHUNK * PAUSE_SECONDS)
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    pause_counter = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_auto() -> str:
    text = ""
    try:
        mic = sr.Microphone() 
        r = sr.Recognizer()
        with mic as source:
            audio = r.listen(source,timeout=2)
        text = r.recognize_google(audio)
    except:
        pass
    finally:
        print(f"Recognized text string of: {text}")
        return text
