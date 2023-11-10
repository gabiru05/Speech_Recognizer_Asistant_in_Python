<a name="readme-top"></a>

<h1 align="center">
  <br>
  Asistente de voz con Azure  <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/SVGs/azure.svg" height="50px" width="50px">
</h1>

<h4 align="center">
Este proyecto utiliza el servicio de reconocimiento de voz de Azure para convertir la voz en texto y realizar algunas acciones según tus ordenes.
</h4>

Reach me at: [![GitHub](https://img.shields.io/badge/GitHub-gabiru05-58f195.svg?logo=github&logoColor=white)](https://github.com/gabiru05)

My OS: ![Windows 11](https://img.shields.io/badge/Windows%2011-0078D6?logo=microsoft&logoColor=white) ![Nobara Linux](https://img.shields.io/badge/Nobara_Linux-000000?logo=linux&logoColor=white)

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Características

-    Reconocimiento de voz en español
-    Responde a comandos simples como "abrir wikipedia", "buscar en google", "que hora es?", etc.
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

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Geopy

```sh
pip install geopy

```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Pynput

```sh
pip install pynput
```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Request

```sh
pip install requests

```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Pycountry

```sh
pip install pycountry

```

-    <img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/bluemark.gif" width="25" alt="Blue Check mark denoting Group Policy">Unidecode

```sh
pip install unidecode


```

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Instalación

-    Clonar el repositorio o descargar el código fuente
-    Instalar las dependencias con el comando `pip install -r requirements.txt` o instalar manualmente los requisitos anteriores
-    Crear una cuenta de Azure y obtener una clave y una región para el servicio de reconocimiento de voz
     Revisa [Este articulo](https://learn.microsoft.com/es-es/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python)
-    Listo ejecutar el archivo `main.py` con el comando `python main.py`

<br>

<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Uso

-    Ejecutar el archivo `main.py` para comenzar a escuchar la voz
-    Hablar al micrófono y esperar a que el texto aparezca en la terminal
-    Presionar el botón "Detener" para terminar de escuchar la voz
-    Mencionar la palabra "Salir" para cerrar el programa

<br>
<img src="https://github.com/gabiru05/Gaby_Resource/blob/master/images/Gifs/1pxRainbowLine.gif" width= "300000" alt="horizontal super thin rainbow RGB line">

## Sección Experimental

**Nota:** Esta sección contiene archivos o funciones experimentales que pueden no funcionar correctamente o generar errores. Utiliza estas herramientas bajo tu propia responsabilidad.

### Pruebas con el Traductor

En esta sección, estoy realizando pruebas con el traductor utilizando las siguientes bibliotecas y los archivos que se encuentran dentro de la carpeta llamada Utilidades_Experimentales:

-    `googletrans` (pip install googletrans)
-    `langdetect` (pip install langdetect)

Ten en cuenta que el funcionamiento de estas bibliotecas puede variar en mis códigos, y no puedo garantizar su estabilidad en todos los casos. Si encuentras problemas o tienes sugerencias para mejorar esta sección, por favor, avísame.
