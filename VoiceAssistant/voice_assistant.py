import VoiceAssistant.input.voice_input as input
import VoiceAssistant.recognition.recognize_speech as recognize
import VoiceAssistant.search.browser as search

def transcribe_seconds():
    def inner(func):
        def wrapper(*args):
            sec = None
            if len(args) == 0:
                sec = 5
            else:
                try:
                    sec = int(args[0])
                except: 
                    print(f"Unable to parse seconds from argument: {args}")
            if sec is not None:
                print(f"Recording for number of seconds: {sec}")
                input.record(sec)

                text = recognize.perform_recognition("output.wav")
                print(f"Transcribed: {text}")

                url = search.create_url(text)
                print(f"Searching for: {url}")
                search.open_tab(url)
            else:
                print(f"Could not generate recording")
        return wrapper
    # returning inner function   
    return inner

def transcribe_auto(func):
    def wrapper(*args):
        print("What would you like to say to me?")
        args = input.record_auto()
        func(args)
    return wrapper
 
@transcribe_seconds()
def transcribe_from_seconds(sec:int) -> str:
    pass

@transcribe_auto
def search_from_text(*args):
    search.open_tab(search.create_url(str(args)))

if __name__ == "__main__":
    #transcribe_from_seconds()
    search_from_text()