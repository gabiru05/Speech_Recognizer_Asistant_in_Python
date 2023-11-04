# Un convertidor de voz a texto y viceversa básico
# Solo funciona con internet
# utiliza google recognition para reconocer la voz
# utiliza la Galería de voz de Microsoft


import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
import webbrowser
import pyttsx3


# Asignamos las funciones que tendra cada variable
recognizer = sr.Recognizer()
engine = pyttsx3.init()
mic = sr.Microphone()

# Configuracion de los servicios de Azure
# Visitar: https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/text-to-speech
# Visitar: https://learn.microsoft.com/es-es/azure/ai-services/speech-service/overview#try-the-speech-service-for-free
# Asignamos las llaves e informacion necesaria para usar los servicios de azure

speech_key = "tu-clave"
service_region = "la-locacion-de-tu-clave"

# Configuramos la secion con datos
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)

# Asignamos la voz preferida
# visitar :https://speech.microsoft.com/   E Ingresar a la galeria de voces para escoger según preferencias
speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"


# Antes de comenzar a utilizar el modelo realizamos un ajuste de audio
with mic as source:
    print("Ajustando audio...")
    recognizer.adjust_for_ambient_noise(source)
    print("Nivel ajustado. Empezemos!!!")


# Definimos la funcion que trasnformara el texto a audio que reciba
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


def Listen():

    with mic as source:
        audio = recognizer.listen(source)

    # Definimos el reconocedor de voz. actualmente es google
    text = recognizer.recognize_google(audio, language='ES')

    print(f'Has dicho: {text}')
    return text.lower()


if 'buenas tardes' in Listen():
    text = 'buenos tardes en que te puedo ayudar?'
    speak(text)
    print("Activacion correcta")

    # Si deseas crear otras funciones u otro codigo luego la idea seria debajo de activar con esa frase.
    # Aun habria que mejorarlo para que funcione con un bucle
