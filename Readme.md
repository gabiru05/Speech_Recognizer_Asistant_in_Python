<a name="readme-top"></a>

<h1 align="center">
  <br>
  Asistente de voz con Azure  <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/SVGs/azure.svg" height="70px" width="100px">
</h1>

<h4 align="center">

Este proyecto utiliza el servicio de reconocimiento de voz de Azure para convertir la voz en texto y realizar algunas acciones según el texto.

</h4>

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Características

-    Reconoce la voz en español e inglés
-    Responde a comandos simples como "abrir wikipedia", "buscar en google", "cerrar la ventana", etc.
-    Tiene una interfaz gráfica simple y amigable para tener idea de las ultimas acciones

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Requisitos

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Python 3.7 o superior
     `Por ahora solamente lo he probado con Python 3.11.6`
     Descarga[Aqui](https://www.python.org/downloads/)

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Azure-cognitiveservices-speech

```sh
 pip install azure-cognitiveservices-speech
```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Py keyboard

```sh
pip install keyboard
```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Pynput

```sh
pip install pynput
```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">PyAudio

```sh
pip install PyAudio
```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Py newspaper3k

```sh
pip install newspaper3k
```

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Instalación

-    Clonar el repositorio o descargar el código fuente
-    Instalar las dependencias con el comando `pip install -r requirements.txt`
-    Crear una cuenta de Azure y obtener una clave y una región para el servicio de reconocimiento de voz
     Revisa [Este articulo](https://learn.microsoft.com/es-es/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python)
-    Crear un archivo `.env` en la carpeta del proyecto y agregar las variables `AZURE_KEY` y `AZURE_REGION` con los valores correspondientes
-    Ejecutar el archivo `Voices_Assistant_Azure_Voices.py` con el comando `python Voices_Assistant_Azure_Voices.py`

<br>

<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Uso

-    Ejecutar el archivo `Voices_Assistant_Azure_Voices ` para comenzar a escuchar la voz
-    Hablar al micrófono y esperar a que el texto aparezca en la terminal
-    Presionar el botón "Detener" para terminar de escuchar la voz
-    Mencionar la palabra "Salir" para cerrar el programa

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
