import sys
import VoiceAssistant.input.voice_input as input
import VoiceAssistant.recognition.recognize_speech as recognize
import VoiceAssistant.search.browser as search

if __name__ == "__main__":
    if len(sys.argv) != 2: #first "real" argument is always the file itself
        print(f"Invalid number of arguments. Expected 2, received: {len(sys.argv)}")
    elif not str(sys.argv[1]).isnumeric():
        print(f"Invalid argment type. Must be Numeric. Received: {sys.argv[1]}")
    else:
        print(f"Recording for number of seconds: {int(sys.argv[1])} (decimals will be ignored)")
        input.record(int(sys.argv[1]))
       
        text = recognize.transcribe("output.wav")
        print(f"Transcribed: {text}")
       
        url = search.create_url(text)
        print(f"Searching for: {url}")

        search.open_tab(url)