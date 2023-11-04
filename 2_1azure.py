'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk 
'''

import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
import webbrowser
import pyttsx3


# Creates an instance of a speech config with specified subscription key and service region.
speech_key = "2763451f17b043e5b4e46fc0f65ecd19"
service_region = "eastus"

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)
# Note: the voice setting will not overwrite the voice element in input SSML.
speech_config.speech_synthesis_voice_name = "es-MX-BeatrizNeural"


recognizer = sr.Recognizer()
engine = pyttsx3.init()


mic = sr.Microphone()

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

    engine. runAndWait()
    text = talk()


# use the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

result = speech_synthesizer.speak_text_async(text).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

    webbrowser.open(f'https://www.amazon.es/{text}')
