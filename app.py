import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('testsuara123.wav')
with harvard as source :
    try :
        audio = r.record(source)
        print(r.recognize_google(audio))
    except:
        print("Suara tidak jelas!")