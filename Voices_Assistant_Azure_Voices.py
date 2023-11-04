import pyttsx3
import keyboard
import webbrowser
import azure.cognitiveservices.speech as speechsdk

# Asignamos las funciones que tendra cada variable

engine = pyttsx3.init()


# Azure service setup
# Asignamos las llaves e informacion necesaria para usar los servicios de azure
speech_key = "d3631e92800a43aba865fa8a654f1b56"
service_region = "eastus"


# Configuramos la secion con datos
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region, speech_recognition_language="es-MX")


# Asignamos la voz preferida
speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"

# Creamos un objeto SpeechRecognizer con el micrófono como fuente de audio
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True))


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

    try:

        # Inicializa el recognizer y espera a que se reconozca el audio
        print("Escuchando...")
        result = speech_recognizer.recognize_once_async().get()
        # Comprueba el resultado
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            # Si se reconoce el audio, devuelve el texto en minúsculas
            text = result.text.lower()
            print(f"Has dicho: {text}")
            return text

        elif result.reason == speechsdk.ResultReason.NoMatch:
            # Si no se reconoce nada, devuelve una cadena vacía
            print("No se ha reconocido nada")
            return ""

        elif result.reason == speechsdk.ResultReason.Canceled:
            # Si se cancela el reconocimiento, muestra el motivo y devuelve una cadena vacía
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(
                cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(
                    cancellation_details.error_details))
            return ""

    except Exception as e:
        # Si ocurre algún error, lo muestra y devuelve una cadena vacía
        print(f"Error: {e}")
        return ""


# Crea un bucle infinito para escuchar continuamente
while True:
    # Escucha el audio
    text = listen()
    print(f"Texto reconocido: {text}")  # Aquí mostramos el texto en la consola
    # Si el texto contiene la palabra clave, activa el asistente
    if text.startswith('good afternoon'):
        saludo = text.replace('asistente', '')
        text = f'{saludo} en qué te puedo ayudar?'
        speak(text)
        print("Activación correcta")

    elif 'wikipedia' in text:

        # Abrir la página web con webbrowser
        url = f'https://wikipedia.org'
        webbrowser.open(url)

    # Si el texto contiene la palabra 'buscar', busca en Google lo que sigue
    elif text.startswith('buscar'):
        # Aquí quitamos la palabra 'buscar' del texto
        query = text.replace('buscar', '')
        # Aquí creamos la url de búsqueda con lo que queda
        url = f'https://www.google.com/search?q={query}'
        webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
        text = f'He buscado {query} en Google'
        speak(text)
        print("Búsqueda realizada")

     # Si el texto contiene la palabra 'abrir', abre la página web que sigue
    elif text.startswith('abrir'):
        # Aquí quitamos la palabra 'abrir' del texto
        url = text.replace('abrir', '')
        webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
        text = f'He abierto {url}'
        speak(text)
        print("Página abierta")

    elif text.startswith('buscar en youtube'):
        # Aquí quitamos la palabra 'buscar en youtube' del texto
        query = text.replace('buscar en youtube', '')
        # Aquí formamos la url de YouTube con el texto que hayas dicho
        url = f'https://www.youtube.com/results?search_query={query}'
        webbrowser.open(url)  # Aquí abrimos la url en el navegador por defecto
        text = f'He buscado {query} en YouTube'
        speak(text)
        print("Búsqueda realizada")

    # Si el texto contiene la palabra 'salir', termina el programa
    elif 'salir' in text:
        text = 'Adiós'
        speak(text)
        keyboard.send('alt+tab')
        print("Programa terminado")
        break  # Aquí salimos del bucle infinito

    elif 'mutea' in text or 'silencia' in text or 'desactiva el audio' in text or 'desactiva el sonido' in text:
        text = 'Silenciando el equipo'
        speak(text)
        keyboard.send('D')  # Silenciar el equipo Hp pavilion

    elif 'desmutea' in text or 'activa el audio' in text or 'desactiva el audio' in text or 'desactiva el sonido' in text:

        keyboard.send('D')  # Silenciar el equipo Hp pavilion
        text = 'Se ha quitado el silencio del equipo'
        speak(text)

    # else:
        # Informar al usuario que el comando no es válido
        # speak("No reconozco ese comando. Por favor, intenta de nuevo.")
