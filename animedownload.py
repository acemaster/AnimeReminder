import requests
payload = {
    'username': 'username',
    'password': 'password'
}
from subprocess import call
while(True):
	with requests.Session() as s:
		s.mount("http://", requests.adapters.HTTPAdapter(max_retries=100))
		s.mount("https://", requests.adapters.HTTPAdapter(max_retries=100))
		s.post('https://kissanime.to/Login', data=payload)
		r = s.get('https://kissanime.to/')
		print r.content
