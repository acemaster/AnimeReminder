#testing
import cfscrape
from lxml import html
import requests
from bs4 import BeautifulSoup
import json


scraper = cfscrape.create_scraper()
def page_scrapper(page2):
	page=scraper.get("http://kissanime.com/AnimeList/NewAndHot?page={0}".format(page2)).content
	# page = requests.get('http://kissanime.com/AnimeList/NewAndHot')
	soup = BeautifulSoup(page, 'html.parser')
	trs=soup.find_all('tr')
	animes={}
	# print trs
	print "Got all the anime of page {0}".format(page2)
	for i in range(0,len(trs)):
		td=trs[i].find_all('a')
		if td:
			animes[td[0].text]={'link': td[0]['href'], 'new_episode': td[1].text }

	json_str=json.dumps(animes)
	with open("AnimeList.txt", "a") as text_file:
	    text_file.write(json_str+'|')


def update_list():
	for i in range(1,5):
		page_scrapper(i)


def getAlist(page):
	with open('AnimeList.txt', 'r') as content_file:
		content = content_file.read()
	contentarr=content.split('|')
	count=1
	name_list=[]
	new_content=json.loads(contentarr[page-1])
	for name,link in new_content.iteritems():
		print str(count)+". "+name[name.index('\n')+1:]
		name_list.append(name)
		count=count+1
	l=raw_input("Enter comma separated list: ")
	l2=l.split(',')
	with open("fav.txt", "a") as text_file:
		for n in l2:
			text_file.write(name_list[int(n)-1]+'|')




# scraper = cfscrape.create_scraper()
# page=scraper.get("http://kissanime.com/Anime/One-Punch-Man").content
# # page = requests.get('http://kissanime.com/AnimeList/NewAndHot')
# soup = BeautifulSoup(page, 'html.parser')
# trs=soup.find_all('tr')
# tds=trs[1].find_all('td')
# print tds