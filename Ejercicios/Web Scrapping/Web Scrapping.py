import requests
from bs4 import BeautifulSoup

# URL de la página web que deseas scrapear
url = "https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado"
page= requests.get(url)

# Crear el objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Guardar el contenido HTML en un archivo
with open("Web Scrapping/pagina_xataka.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# Extraer y guardar el título de la página
titulo = soup.h1.string

# Guardar el título en un archivo de texto
with open("Web Scrapping/titulo_xataka.txt", "w", encoding="utf-8") as fileTitulo:
    fileTitulo.write(titulo)

# Extraer y guardar el primer elemento de lista <li>
li = soup.find_all('li')

with open("Web Scrapping/li_xataka.txt", "w", encoding="utf-8") as fileLi:
    for item in li:
        fileLi.write(item.get_text() + "\n")