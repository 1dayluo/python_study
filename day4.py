import requests
import webbrowser
import time


api = 'https://api.github.com/users/kennethreitz/starred'

starred_page = []

info = requests.get(api).json()
for i in info:
    starred_page.append(i['id'])

while True:
   info = requests.get(api).json()
   for i in info:
       if not i['id'] in starred_page:
           repo_name = i['name' ]
           owner = i['owner']['login']
           web_page = "https://github.com/" + owner + "/" + repo_name
           webbrowser.open(web_page)
   time.sleep(600)