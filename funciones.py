import requests
import geocoder
import pycountry
import unidecode
import webbrowser
import time
import azure.cognitiveservices.speech as speechsdk
from geopy.geocoders import Nominatim


def leer_noticias():
    api_key = "pub_32426bda3f7549b2e7bcdc1ed8c3459f06059"
    g = geocoder.ip('me')
    lat, lon = g.latlng
    geoLoc = Nominatim(user_agent="GetLoc")
    locname = geoLoc.reverse(f"{lat}, {lon}")
    country_name = locname.raw["address"]["country"]
    mapping = {unidecode.unidecode(country.name.lower(
    )): country.alpha_2 for country in pycountry.countries}
    country_code = mapping.get(unidecode.unidecode(country_name.lower()))
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&country={country_code}"
    data = requests.get(url).json()
    if "results" in data:
        results = data["results"]
        seq = ['primera', 'segunda', 'tercera', 'cuarta', 'quinta',
               'sexta', 'séptima', 'octava', 'novena', 'décima']
        headings = []
        for res in results:
            headings.append(res['title'])

        speak("¿Cuántas noticias deseas escuchar?")
        cantidad = None

        while cantidad is None:
            text = listen()
            print(f"Texto reconocido: {text}")
            if text.isdigit():
                cantidad = int(text)
                if cantidad > 0 and cantidad <= len(seq):
                    for i in range(cantidad):
                        num_seleccionado = i
                        leer_noticia(num_seleccionado, results)

                        if i < cantidad - 1:
                            speak(
                                "¿Deseas escuchar la siguiente noticia o leer más sobre alguna noticia en particular?")
                            while True:
                                text = listen()
                                print(f"Texto reconocido: {text}")
                                if "cancelar" in text:
                                    speak("Lectura de noticias cancelada.")
                                    return
                                elif "sí" in text:
                                    break
                                elif "no" in text:
                                    break
                                else:
                                    speak(
                                        "Por favor, di 'sí' para la leer la siguiente noticia o 'no' para detener la lectura.")
                else:
                    speak(
                        "Por favor, solo menciona un número que sea válido dentro del rango de noticias disponibles.")
            else:
                speak(
                    "Por favor, solo menciona un número que sea válido dentro del rango de noticias disponibles.")

        speak("No hay más noticias disponibles.")


def leer_noticia(num_seleccionado, results):
    # Obtenemos el contenido de la noticia usando el índice
    contenido = results[num_seleccionado]["content"]
    speak(contenido)


def buscar_en_google(query):
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    text = f'He buscado {query} en Google'
    speak(text)
    print("Búsqueda realizada")


def abrir_pagina_web(url):
    webbrowser.open(url)
    text = f'He abierto {url}'
    speak(text)
    print("Página abierta")


# Configuración de Azure
speech_key = "d3631e92800a43aba865fa8a654f1b56"
service_region = "eastus"
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region, speech_recognition_language="es-MX")
# Configuramos la voz de preferencia:
speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"
# speech_config.speech_synthesis_voice_name = "es-MX-DaliaNeural"

speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True))

# Funcion para narrar texto


def speak(text):
    # Aplicamos las configuraciones de idioma y voz previas
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()
    # Comprobamos el result de la transcripcion
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(
            cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(
                cancellation_details.error_details))


def saludar():
    ahora = time.localtime()
    hora = ahora.tm_hour
    saludo = ""
    if hora < 12:
        saludo = "Buenos días"
    elif hora < 18:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    return saludo


# Función para escuchar y reconocer el audio

def listen():
    try:
        print("Escuchando...")
        result = speech_recognizer.recognize_once_async().get()
        # Inicializa el recognizer y espera a que se reconozca el audio
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
           # devolvemos el texto en minúscula y eliminamos el punto final de la oraciones
            text = result.text.lower()
            if text.endswith('.'):
                text = text[:-1]
            print(f"Has dicho: {text}")
            return text
         # Si no se reconoce nada, devuelve una cadena vacía
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No se ha reconocido nada")
            return ""
         # Si se cancela el reconocimiento, muestra el motivo y devuelve una cadena vacía
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(
                cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(
                    cancellation_details.error_details))
            return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""


def buscar_en_youtube(query):
    url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(url)
    text = f'He buscado {query} en YouTube'
    speak(text)
    print("Búsqueda realizada")


def hora():
    ahora = time.localtime()
    hora = ahora.tm_hour
    minuto = ahora.tm_min
    text = f"Son las {hora} y {minuto}"
    speak(text)
