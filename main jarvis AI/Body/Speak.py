# speek fuctions
# windows voice .pyttsx3 
# chrome voice  pip install selenium

# windows base
import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"AI: {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()
    





#Speak("Welcome sir how can help you")