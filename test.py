#testing
import cfscrape
from lxml import html
import requests
from bs4 import BeautifulSoup


scraper = cfscrape.create_scraper()
page=scraper.get("http://kissanime.com/AnimeList/NewAndHot").content
# page = requests.get('http://kissanime.com/AnimeList/NewAndHot')
soup = BeautifulSoup(page, 'html.parser')
trs=soup.find_all('tr')
animes={}
# print trs
print "Got all the anime of page 1"
for i in range(0,len(trs)):
	td=trs[i].find('a')
	if td:
		animes[td.text]=td['href']

# print animes

# scraper = cfscrape.create_scraper()
page=scraper.get("http://kissanime.com/Anime/One-Punch-Man").content
# page = requests.get('http://kissanime.com/AnimeList/NewAndHot')
soup = BeautifulSoup(page, 'html.parser')
trs=soup.find_all(id="nextEpisodeCountDown")
print trs