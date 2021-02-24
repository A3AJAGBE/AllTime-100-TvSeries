"""Scraping Stacker Website for the article on the best 100 tv shows ever"""

import requests
from bs4 import BeautifulSoup

STACKER_URL = 'https://stacker.com/stories/980/100-best-tv-shows-all-time'

response = requests.get(STACKER_URL)
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
tv_shows = soup.find_all(name="h2")
tv_titles = [tv.getText() for tv in tv_shows[3:-1]]
# Reverse the order of the list
tv_titles_asc = tv_titles[::-1]

# Add the list to txt file
with open("tvShows.txt", mode="w") as file:
    for tv in tv_titles_asc:
        file.write(f"{tv}\n")