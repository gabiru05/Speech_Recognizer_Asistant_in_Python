import speech_recognition as sr
from langdetect import detect
# Importa la biblioteca googletrans
from googletrans import Translator


# Crea una instancia de Recognizer
r = sr.Recognizer()

# Usa el micrófono como fuente de audio
with sr.Microphone() as source:
    # Escucha el audio del usuario
    audio = r.listen(source)

# Reconoce el habla del usuario usando Google Cloud Speech API
result = r.recognize_google(audio, show_all=True)

# Obtiene la mejor transcripción del audio
transcript = result["alternative"][0]["transcript"]

# Detecta el idioma de la transcripción
language = detect(transcript)

# Imprime el idioma detectado
print(language)
