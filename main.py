from funciones import (
    saludar, listen, speak, buscar_en_youtube, leer_noticias, buscar_en_google, abrir_pagina_web, hora
)
import azure.cognitiveservices.speech as speechsdk
import requests
import webbrowser
from pynput.keyboard import Key, Controller


# Iniciamos el teclado
keyboard = Controller()


def main():
    text = saludar()
    speak(text)
    while True:
        text = listen()
        print(f"Texto reconocido: {text}")
        if any(keyword in text for keyword in ["buenos días", "buenos dias", "buen día", "buenas tardes", "buenas tarde", "buena tarde"]):

            text = 'en qué te puedo ayudar?'
            speak(text)
            print("Activación correcta")
            while True:

                text = listen()
                print(f"Texto reconocido: {text}")

                # Tiempo
                if 'hora' in text:
                    hora()

                elif 'abrir wikipedia' in text:
                    url = f'https://wikipedia.org'
                    webbrowser.open(url)

                elif 'leer noticia' in text:
                    leer_noticias()

                # Si el texto contiene la palabra 'buscar', busca en Google lo que sigue
                elif text.startswith('buscar en google'):
                    query = text.replace('buscar en google', '')
                    buscar_en_google(query)

                # Abrira el explorador para investigar
                elif text.startswith('investigar'):
                    url = text.replace('investigar', '')
                    abrir_pagina_web(url)

                elif text.startswith('buscar en youtube'):
                    query = text.replace('buscar en youtube', '')
                    buscar_en_youtube(query)

                elif 'salir' in text:
                    text = 'Adiós'
                    speak(text)
                    keyboard.press(Key.alt)
                    keyboard.press(Key.tab)
                    keyboard.release(Key.alt)
                    keyboard.release(Key.tab)
                    print("Programa terminado")
                    break


if __name__ == "__main__":
    main()
