from bs4 import BeautifulSoup
from lxml import etree
from io import StringIO, BytesIO
import requests
from time import sleep
import random

from base import update_anime
from config import linck

img_domain = "https://animestars.org"

while (True):
    sleep(180) #3минут
    id = 0
    i = random.randint(1, 76)
    url = f'{linck}{i}/'
    html = requests.get(url)
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
        img = img_domain + img
        update_anime(title, year, genre, link, description, img, id)
        id += 1
