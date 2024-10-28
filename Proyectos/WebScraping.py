import requests
from bs4 import BeautifulSoup

URL = "https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

titulo = soup.title.string
print("Titulo de la pagina:", titulo)

lista = soup.find_all("li", class_="masthead-nav-topics-item")
for li in lista:
    print("Elemento <li>:", li.text.strip())

contenido = soup.find("div", class_="article-content")
if contenido:
    for em in contenido.find_all("em"):
        em.decompose()
    limpiaTexto = contenido.get_text(separator="\n", strip=True)
    print("Texto de la noticia:\n", limpiaTexto)
else:
    print("No se encontro el contenido de la noticia")
