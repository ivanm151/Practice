from bs4 import BeautifulSoup
import requests
import logging
"""Обработка ошибок"""


def process():
    """Извлечение десяти популярных песен исполнителя"""
    url_author = input("Введите ссылку на исполнителя на Яндекс-музыке: ")
    try:
        page = requests.get(url_author + "/tracks")
    except requests.exceptions.RequestException as a:
        logging.error(a)
        return
    for obj in BeautifulSoup(page.text, "html.parser").find_all('div', class_='d-track')[:10]:
        print(obj.find('a', class_='d-track__title').text.strip())


process()
# url_example = "https://music.yandex.ru/artist/36825"  # Radiohead
