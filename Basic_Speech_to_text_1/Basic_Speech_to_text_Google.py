# Un convertidor de voz a texto básico utilizando google recognition
# Solo funciona con internet
import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language='ES')

print(f'Has dicho: {text}')
