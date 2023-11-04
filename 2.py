import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

mic = sr.Microphone()

# Cambiar la voz a español de España
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')

# Ajustar el umbral de energía manualmente
# recognizer.energy_threshold = 300

# Ajustar el umbral de energía automáticamente según el ruido ambiental
with mic as source:
    print("ajustando audio")
    recognizer.adjust_for_ambient_noise(source)
    print("voz ajustada. empezamos")


def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)
        
    text = recognizer.recognize_google(audio, language='ES')

    print(f'Has dicho: {text}')
    return text.lower()


if 'amazon' in talk():
    engine.say('Bienvenido a Amazon, ¿qué quieres comprar?')
    engine. runAndWait()
    text = talk()
    webbrowser.open(f'https://www.amazon.es/{text}')
