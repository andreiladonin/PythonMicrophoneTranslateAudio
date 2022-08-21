import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


r = sr.Recognizer()

with sr.Microphone() as source:
    print("ГОВОРИ ")
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=15)
    print('Он определяет ваш голос…')
    text = r.recognize_google(data, language="ru")
    print(text)

    var = gTTS(text=text, lang='ru')
    var.save('ru.mp3')
    playsound('ru.mp3')