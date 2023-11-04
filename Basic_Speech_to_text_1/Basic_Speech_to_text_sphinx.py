# Un convertidor de voz a texto básico utilizando Sphinx
# funciona sin internet (Requiere mayor configuración)
# Instalar en consola: pip install vosk
# Solo viene con un modelo en ingles tendras descargar otros segun tu necesidad
# Noes tan preciso el modelo que trae por defecto o suceptible a mucho ruido
import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()


with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    print("voz ajustada. empezamos")
    audio = recognizer.listen(source)

text = recognizer.recognize_sphinx(audio, language='en-US')

print(f'Has dicho: {text}')
