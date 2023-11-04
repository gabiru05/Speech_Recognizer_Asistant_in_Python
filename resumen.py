# Importamos la librería Newspaper3k para extraer el contenido principal de un artículo web
from newspaper import Article

# Definimos una función que recibe una URL como parámetro y devuelve el título, el autor y el texto del artículo


def extraer_contenido(url):
    # Creamos un objeto Article con la URL
    articulo = Article(url)
    # Descargamos el contenido HTML de la página
    articulo.download()
    # Analizamos el contenido HTML y extraemos los datos relevantes
    articulo.parse()
    # Devolvemos el título, el autor y el texto del artículo como una tupla
    return articulo.title, articulo.authors, articulo.text


# Probamos la función con un ejemplo de URL
url = "https://www.bbc.com/news/world-us-canada-67317218"
titulo, autor, texto = extraer_contenido(url)

# Imprimimos el resultado
print("Título:", titulo)
print("Autor:", autor)
print("Texto:", texto)
