import webbrowser

def create_url(text) -> str:
    #Assumes Google.com search result
    prefix = "www.google.com/search?q="
    return prefix + text.replace(" ", "+")

def open_tab(url):
    webbrowser.open_new_tab(url)