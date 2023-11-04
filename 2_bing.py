import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

mic = sr.Microphone()
bing_key = '2763451f17b043e5b4e46fc0f65ecd19'
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
        # Definir la variable audio
        audio = recognizer.listen(source)
        text = recognizer.recognize_bing(
            audio, key=bing_key, language='ES', location='eastus')

    print(f'Has dicho: {text}')
    return text.lower()


# Asignar el resultado de talk() a una variable
voice_input = talk()

if 'amazon' in voice_input:
    engine.say('Bienvenido a Amazon, ¿qué quieres comprar?')
    engine.runAndWait()
    text = talk()
    # Reemplazar los espacios por signos de más
    webbrowser.open(f'https://www.amazon.es/{text.replace(" ", "+")}')
