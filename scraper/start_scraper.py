from bs4 import BeautifulSoup
from lxml import etree
from io import StringIO, BytesIO
import requests
from time import sleep

from base import add_anime

for p in range(1, 3):
    url = f"https://animestars.org/page/{p}/"
    html = requests.get(url)
    sleep(5)
    soup = BeautifulSoup(html.text, 'lxml')

    animes = soup.find('div', id='dle-content').findAll('a', class_='poster grid-item d-flex fd-column has-overlay')

    for anime in animes:
        link = anime.get('href')
        title = anime.find('div', class_='poster__desc').find('h3', class_='poster__title ws-nowrap').text
        year = anime.find('div', class_='poster__desc').find('div', class_='poster__subtitle d-flex ai-center').find('div', class_='poster__meta flex-grow-1 ws-nowrap').text.split(',')[0]
        year = "".join(year)
        genre = anime.find('div', class_='poster__desc').find('div', class_='poster__subtitle d-flex ai-center').find('div', class_='poster__meta flex-grow-1 ws-nowrap').text.split(',')[1:]
        genre = ",".join(genre)
        description = anime.find('div', class_='poster__desc').find('div', class_='poster__subtitle d-flex ai-center').find('div', style='display: none;').text
        img = anime.find('img', class_='lazy-loaded').get('data-src')
        img = "https://animestars.org" + img
        add_anime(title, year, genre, link, description, img)
