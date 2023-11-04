import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
import webbrowser
import pyttsx3


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

# Definimos el reconocedor de voz. actualmente es google


def talk():

    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='ES')

    print(f'Has dicho: {text}')
    return text.lower()


if 'buenas tardes' in talk():
    text = 'buenos dias en que te puedo ayudar?'
    speak(text)
    print("Activacion correcta")
