import requests
from bs4 import BeautifulSoup

import re

# URL del sitio web que deseas extraer
url = "https://oxxo.com/contacto"

# Realiza la solicitud HTTP al sitio web
response = requests.get(url)

# Verifica que la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crea un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrae todo el texto del sitio web
    text = soup.get_text()

    regex_email = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex_phone_number = r"(\(\+?\d{2,3}\)[\*|\s|\-|\.]?(([\d][\*|\s|\-|\.]?){6})(([\d][\s|\-|\.]?){2})?|(\+?[\d][\s|\-|\.]?){8}(([\d][\s|\-|\.]?){2}(([\d][\s|\-|\.]?){2})?)?)"

    res = re.search(regex_email, text)
    print(res.group(0))

else:
    print(f"Error al acceder al sitio web: {response.status_code}")
