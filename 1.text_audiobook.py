"""importing required modules """
import pyttsx3


def text_audio():
    """function for text to audio conversion"""

    with open("text_audio.txt", "r", encoding="utf8") as textfile:
        female_voice = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech" \
                r"\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"            #link for female voice
        obj1 = pyttsx3.init() #initialize the object for pyttsx3
        text = textfile.read()  #reading content of a file and placing in "text" obj
        obj1.setProperty("rate", 200)  # setProperty() used to increase speach speed
        obj1.setProperty('voice', female_voice)
        print(text)
        obj1.say(text)          #say() function used to speak
        obj1.runAndWait()

text_audio()
