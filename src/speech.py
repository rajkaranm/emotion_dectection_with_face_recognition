import pyttsx3
import speech_recognition as sr


def recognized_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        return query

    except Exception as e:
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
