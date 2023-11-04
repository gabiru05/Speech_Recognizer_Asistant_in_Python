import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()


with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("voz ajustada. empezamos")
    audio = recognizer.listen(source)

text = recognizer.recognize_sphinx(audio, language='en-US')


print(f'Has dicho: {text}')
