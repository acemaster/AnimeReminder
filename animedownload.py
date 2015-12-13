import requests
import cfscrape
from lxml import html
import requests
from bs4 import BeautifulSoup
import json

payload = {
    'username': 'acemastervv',
    'password': 'vivek123'
}
scraper = cfscrape.create_scraper()
from subprocess import call
with requests.Session() as s:
	s.mount("http://", requests.adapters.HTTPAdapter(max_retries=100))
	s.mount("https://", requests.adapters.HTTPAdapter(max_retries=100))
	s.post('https://kissanime.to/Login', data=payload)
	page=scraper.get("https://kissanime.to/Anime/One-Punch-Man/Episode-011").content
	soup = BeautifulSoup(page, 'html.parser')
	div=soup.find_all('div', id='divDownload')
	print div
