import pyttsx3
import webbrowser
import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk

# Asignamos las funciones que tendra cada variable
recognizer = sr.Recognizer()
engine = pyttsx3.init()
mic = sr.Microphone()

# Azure service setup
# Asignamos las llaves e informacion necesaria para usar los servicios de azure
speech_key = "2763451f17b043e5b4e46fc0f65ecd19"
service_region = "eastus"

# Configuramos la secion con datos
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)

# Asignamos la voz preferida
speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"


# Antes de comenzar a utilizar el modelo realizamos un ajuste de audio
with mic as source:
    print("Ajustando audio...")
    recognizer.adjust_for_ambient_noise(source)
    print("Nivel ajustado. Empezemos!!!")


def speak(text):

    # Utilizamos la voz preferida por defecto
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(
            cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(
                cancellation_details.error_details))
# Define una función para escuchar y reconocer el audio


def listen():
    with mic as source:
        audio = recognizer.listen(source)
    try:
        # Usa el reconocimiento offline con CMU Sphinx
        text = recognizer.recognize_google(audio, language='ES')
        print(f"Has dicho: {text}")
        return text.lower()
    except sr.UnknownValueError:
        # Si no se reconoce nada, devuelve una cadena vacía
        return ""


# Crea un bucle infinito para escuchar continuamente
while True:
    # Escucha el audio
    text = listen()
    print(f"Texto reconocido: {text}")  # Aquí mostramos el texto en la consola
    # Si el texto contiene la palabra clave, activa el asistente
    if 'hola' in text:
        saludo = text.split()[0]
        text = f'{saludo} en qué te puedo ayudar?'
        speak(text)
        print("Activación correcta")
    # Si el texto contiene la palabra 'buscar', busca en Google lo que sigue
    elif 'buscar' in text:
        # Aquí quitamos la palabra 'buscar' del texto
        query = text.replace('buscar', '')
        # Aquí creamos la url de búsqueda con lo que queda
        url = f'https://www.google.com/search?q={query}'
        webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
        text = f'He buscado {query} en Google'
        speak(text)
        print("Búsqueda realizada")
    # Si el texto contiene la palabra 'abrir', abre la página web que sigue
    elif 'abrir' in text:
        # Aquí quitamos la palabra 'abrir' del texto
        url = text.replace('abrir', '')
        webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
        text = f'He abierto {url}'
        speak(text)
        print("Página abierta")
    # Si el texto contiene la palabra 'salir', termina el programa
    elif 'salir' in text:
        text = 'Adiós'
        speak(text)
        print("Programa terminado")
        break  # Aquí salimos del bucle infinito
