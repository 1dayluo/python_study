import requests
from datetime import datetime
from datetime import timedelta
#repo_api = 'https://api.github.com/search/repositories?q=size:<200+language:'

def get_code(repo):
    code_api = 'https://api.github.com/search/code?q=in:both+language:python++size:<200+repo:'
    #print('Please input the language you want')
    #choice_lang = input()
    choice_lang = "python"
    items = requests.get(code_api+repo).json()['items']
    for item in items:
        repo_name = item['repository']['full_name']
        repo_url = item['html_url']
        print(repo_name + ':  ' + repo_url)

def get_rep():
    repo_api = 'https://api.github.com/search/repositories?q=language:python+created:>'
    all_info = requests.get(repo_api).json()
    #判断是最近一周的
    now = datetime.now()

    last_week = str(now - timedelta(days=now.isoweekday())).split()[0]
    all_info = requests.get(repo_api+last_week).json()

    for info in all_info['items']:
        updated_time = info['created_at']

        #if updated_time > last_week:

        get_code(info['full_name'])





get_rep()




