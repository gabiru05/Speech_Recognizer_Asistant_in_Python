import time
import pyttsx3
from newspaper import Article
import keyboard
import webbrowser
import azure.cognitiveservices.speech as speechsdk
from pynput.keyboard import Key, Controller
import requests
# Importamos la librería unidecode
import unidecode


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

# Iniciamos el teclado
keyboard = Controller()


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
            # Elimina el punto final de la cadena si existe
            if text.endswith('.'):
                text = text[:-1]
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


def saludar():
    # Obtenemos el momento actual del sistema
    ahora = time.localtime()
    # Obtenemos la hora actual
    hora = ahora.tm_hour
    # Creamos una variable para guardar el saludo
    saludo = ""
    # Dependiendo de la hora, asignamos un saludo diferente
    if hora < 12:
        saludo = "Buenos días"
        return saludo
    elif hora < 18:
        saludo = "Buenas tardes"
        return saludo
    else:
        saludo = "Buenas noches"
        return saludo


# Creamos el texto que vamos a decir
text = saludar()
# Usamos la función speak para decir el texto
speak(text)


# Crea un bucle infinito para escuchar continuamente
while True:

    # Escucha el audio
    text = listen()
    print(f"Texto reconocido: {text}")  # Aquí mostramos el texto en la consola

    # Si el texto contiene la palabra clave, activa el asistente
    if "buenos días" in text or "buenos dias" in text or "buen día" in text:
        saludo = text.replace('asistente', '')
        text = f'{saludo} en qué te puedo ayudar?'
        speak(text)
        print("Activación correcta")
        while True:
            text = listen()
            # Aquí mostramos el texto en la consola
            print(f"Texto reconocido: {text}")
            if 'hora' in text:
                # Obtenemos el momento actual del sistema
                ahora = time.localtime()
                # Obtenemos la hora actual
                hora = ahora.tm_hour
                minuto = ahora.tm_min
                # Creamos el texto que vamos a decir
                text = f"Son las {hora} y {minuto}"
                # Usamos la función speak para decir el texto
                speak(text)

            elif 'wikipedia' in text:

                # Abrir la página web con webbrowser
                url = f'https://wikipedia.org'
                webbrowser.open(url)

            elif 'leer noticia' in text:
                # Importamos las librerías necesarias
                import requests
                import geocoder
                import pycountry
                import unidecode
                from geopy.geocoders import Nominatim
                # Definimos nuestra clave de la API de newsdata.io
                api_key = "pub_32426bda3f7549b2e7bcdc1ed8c3459f06059"
                # Obtenemos las coordenadas del usuario usando geocoder
                g = geocoder.ip('me')
                lat, lon = g.latlng
                # Obtenemos el nombre del país usando Nominatim
                geoLoc = Nominatim(user_agent="GetLoc")
                locname = geoLoc.reverse(f"{lat}, {lon}")
                country_name = locname.raw["address"]["country"]
                print(country_name)
                # Convertimos el nombre del país a su código ISO usando pycountry y unidecode
                mapping = {unidecode.unidecode(country.name.lower(
                )): country.alpha_2 for country in pycountry.countries}
                country_code = mapping.get(
                    unidecode.unidecode(country_name.lower()))
                print(country_code)
                # Definimos la URL de la API con nuestra clave y el parámetro de país
                url = f"https://newsdata.io/api/1/news?apikey={api_key}&country={country_code}"
                # Obtenemos la respuesta JSON de la API
                data = requests.get(url).json()
                # Comprobamos si hay resultados en la respuesta
                if "results" in data:
                    # Extraemos la lista de resultados
                    results = data["results"]
                    # Creamos una lista vacía para almacenar los títulos
                    headings = []
                    # Creamos una lista con los números ordinales en español
                    seq = ['primera', 'segunda', 'tercera', 'cuarta', 'quinta',
                           'sexta', 'séptima', 'octava', 'novena', 'décima']
                    # Recorremos la lista de resultados y añadimos los títulos a la lista de headings
                    for res in results:
                        headings.append(res['title'])
                    # Recorremos la lista de headings y leemos cada título usando azure
                    for i in range(len(seq)):
                        print(f"La {seq[i]} noticia de hoy es: {headings[i]}")
                        speak(f"La {seq[i]} noticia de hoy es: {headings[i]}")
                    # Terminamos la lectura con un mensaje final
                    # Modificamos el código para que después de leer los títulos, pregunte al usuario si quiere leer más sobre alguna noticia

                    # Modificamos el código para que después de leer los títulos, pregunte al usuario si quiere leer más sobre alguna noticia
                    speak("He terminado, he leído la mayoría de las últimas noticias")
                    speak("¿Quiere leer más sobre alguna noticia?")
                    text = listen()
                    # Creamos una variable para controlar el bucle
                    valid = False
                    # Mientras la respuesta no sea válida, seguimos preguntando
                    while not valid:
                        if "sí" in text or "si" in text:
                            speak("¿Sobre cuál noticia quiere leer más?")

                            text = listen()

                            # Creamos un diccionario que asocia los números ordinales con los índices
                            ordinales = {'primera': 0, 'segunda': 1, 'tercera': 2, 'cuarta': 3,
                                         'quinta': 4, 'sexta': 5, 'septima': 6, 'octava': 7, 'novena': 8, 'decima': 9}

                            # Obtenemos el índice de la noticia
                            for num in ordinales:
                                if num in text:
                                    # ordinales es el diccionario que definiste antes
                                    indice = ordinales.get(num)

                            # Imprimimos el valor de indice
                            print(f"Indice: {indice}")
                            # Comprobamos si el índice es válido
                            if indice is not None:
                                # Definimos una función que lee el contenido de una noticia
                                def leer_noticia(indice):
                                    # Obtenemos el contenido de la noticia usando el índice
                                    contenido = data["results"][indice]["content"]
                                    # Leemos el contenido usando azure
                                    speak(contenido)
                                # Llamamos a la función que lee la noticia
                                leer_noticia(indice)
                                # Marcamos la respuesta como válida y salimos del bucle
                                valid = True
                            else:
                                # El usuario no ha dicho un número ordinal válido
                                speak(
                                    "Lo siento, no he entendido sobre qué noticia quiere leer más")
                                # Volvemos a pedir el audio al usuario
                                text = listen()
                        elif "no" in text:
                            # El usuario no quiere leer más sobre ninguna noticia
                            speak("Está bien, no hay problema")
                            # Marcamos la respuesta como válida y salimos del bucle
                            valid = True
                        else:
                            # El usuario no ha dicho ni sí ni no
                            speak(
                                "Lo siento, no he entendido su respuesta. ¿Quiere leer más sobre alguna noticia?")
                            # Volvemos a pedir el audio al usuario
                            text = listen()

                else:
                    # No hay resultados para el país del usuario
                    speak(
                        f"Lo siento, no hay noticias disponibles para {country_name}")

            # Si el texto contiene la palabra 'buscar', busca en Google lo que sigue
            elif text.startswith('buscar en google'):
                # Aquí quitamos la palabra 'buscar' del texto
                query = text.replace('buscar en google', '')
                # Aquí creamos la url de búsqueda con lo que queda
                url = f'https://www.google.com/search?q={query}'
                # Aquí abrimos la url en el navegador por defecto
                webbrowser.open(url)
                text = f'He buscado {query} en Google'
                speak(text)
                print("Búsqueda realizada")

            # Si el texto contiene la palabra 'abrir', abre la página web que sigue
            elif text.startswith('abrir'):
                # Aquí quitamos la palabra 'abrir' del texto
                url = text.replace('abrir', '')
                # Aquí abrimos la url en el navegador por defecto
                webbrowser.open(url)
                text = f'He abierto {url}'
                speak(text)
                print("Página abierta")

            elif text.startswith('buscar en youtube'):
                # Aquí quitamos la palabra 'buscar en youtube' del texto
                query = text.replace('buscar en youtube', '')
                # Aquí formamos la url de YouTube con el texto que hayas dicho
                url = f'https://www.youtube.com/results?search_query={query}'
                # Aquí abrimos la url en el navegador por defecto
                webbrowser.open(url)
                text = f'He buscado {query} en YouTube'
                speak(text)
                print("Búsqueda realizada")
            elif 'salir' in text:
                text = 'Adiós'
                speak(text)
                keyboard.press(Key.alt)  # Presiona la tecla Alt
                keyboard.press(Key.tab)  # Presiona la tecla Tab
                keyboard.release(Key.alt)  # Suelta la tecla Alt
                keyboard.release(Key.tab)  # Suelta la tecla Tab
                print("Programa terminado")
                break  # Aquí salimos del bucle infinito

    # Si el texto contiene la palabra 'salir', termina el programa
    elif 'salir' in text:
        text = 'Adiós'
        speak(text)
        keyboard.press(Key.alt)  # Presiona la tecla Alt
        keyboard.press(Key.tab)  # Presiona la tecla Tab
        keyboard.release(Key.alt)  # Suelta la tecla Alt
        keyboard.release(Key.tab)  # Suelta la tecla Tab
        print("Programa terminado")
        break  # Aquí salimos del bucle infinito

    elif 'mutea' in text or 'silencia' in text or 'desactiva el audio' in text or 'desactiva el sonido' in text:
        text = 'Silenciando el equipo'
        speak(text)
        # keyboard.send('D')  # Silenciar el equipo Hp pavilion

        keyboard.press(Key.media_volume_mute)  # Presiona la tecla de silencio
        keyboard.release(Key.media_volume_mute)  # Suelta la tecla de silencio

    elif 'desmutea' in text or 'activa el audio' in text or 'desactiva el audio' in text or 'activa el sonido' in text:

        # keyboard.send('D')  # Quitar el silecio equipo Hp pavilion
        keyboard.press(Key.media_volume_mute)  # Presiona la tecla de silencio
        keyboard.release(Key.media_volume_mute)  # Suelta la tecla de silencio
        text = 'Se ha quitado el silencio del equipo'
        speak(text)

    # else:
        # Informar al usuario que el comando no es válido
        # speak("No reconozco ese comando. Por favor, intenta de nuevo.")
