# listion in kannada reply in english

# pip install googletrans
import speech_recognition as sr  # pip install SpeechRecognition
from googletrans import Translator

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listion......')
        r.phrase_threshold = 1
        audio = r.listen(source)

    try :
       
       print('recognise....')
       query= r.recognize_google(audio,language="en-in")
       
    
    except :
        return""
    query=str(query).lower()
    return query

#print(listen())

# 2 - Translation

def TranslationknToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect

# connect
def MicExecution():

    query = listen()
    data = (query)
    return data

