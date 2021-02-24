"""Scraping Empire Website for the article on the best tv shows ever"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/tv/features/best-tv-shows-ever-2/')
response.raise_for_status()
data = response.text