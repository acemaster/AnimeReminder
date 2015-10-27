import dryscrape

# make sure you have xvfb installed
dryscrape.start_xvfb()

search_term = 'dryscrape'

# set up a web scraping session
sess = dryscrape.Session(base_url = 'http://kissanime.com/Anime/One-Punch-Man')

# we don't need images
sess.set_attribute('auto_load_images', False)

# visit homepage and search for a term
print sess.visit('/')