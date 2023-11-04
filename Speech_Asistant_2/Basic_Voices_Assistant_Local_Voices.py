# Un convertidor de voz a texto y viceversa básico
# Solo funciona con internet
# utiliza google recognition para reconocer la voz
# utiliza el lenguaje de tu equipo para narrar la voz

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
mic = sr.Microphone()

# Cambiar la voz a español de mexico
# Nota: debes tener instalado la voz o cambiar segun el idioma de tu equipo
# Para mayor información revisar: https://stackoverflow.com/questions/65977155/change-pyttsx3-language
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')


# Ajustar el umbral de energía automáticamente según el ruido ambiental
with mic as source:
    print("ajustando audio")
    recognizer.adjust_for_ambient_noise(source)
    print("voz ajustada. empezamos")


def Listen():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='ES')

    print(f'Has dicho: {text}')
    return text.lower()


if 'buscar' in Listen():
    engine.say('Bienvenido, ¿qué quieres buscar?')
    engine.runAndWait()
    text = Listen()
    # Aquí creamos la url de búsqueda con lo que queda

    url = f'https://www.google.com/search?q={text}'
    webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
    engine.say('He realizado tu busqueda en Google')
    engine.runAndWait()
    print("Búsqueda realizada")
