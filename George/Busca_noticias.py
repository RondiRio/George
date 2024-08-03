import requests
from bs4 import BeautifulSoup
def noticias():
    url = 'https://www.globo.com/'
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # Encontrar todos os h2 com a classe 'post_title'
    noticia_elements = soup.find_all('h2', class_='post_title')
    disc = {}
    if noticia_elements:
        for noticia in noticia_elements:
            a_tag = noticia.find('a')
            if a_tag:
                titulo = a_tag.get_text(strip=True)
                link = a_tag.get('href')
                if titulo and link:
                    disc[titulo] = link
    else:
        print("Nenhuma notícia encontrada com a classe 'post_title'.")
    return disc
news = noticias()
if news:
    for titulo, link in news.items():
        print(f'{titulo}: {link}')
else:
    print("Nenhuma notícia encontrada.")