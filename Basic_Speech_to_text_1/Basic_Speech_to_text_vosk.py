# Un convertidor de voz a textobásico utilizando vosk
# funciona sin internet (Requiere mayor configuración)
import vosk
import pyaudio

model = vosk.Model("vosk-model-small-es-0.3")
rec = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(f'Has dicho: {result["text"]}')
