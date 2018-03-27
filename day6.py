import requests
from datetime import datetime
from datetime import timedelta

def make_message(item):
    pass
def get_rep():
    repo_api = 'https://api.github.com/search/repositories?q=topic:django+created:>'
    all_info = requests.get(repo_api).json()
    #判断是最近一周的
    now = datetime.now()

    last_week = str(now - timedelta(days=now.isoweekday())).split()[0]
    all_info = requests.get(repo_api+last_week).json()

    for info in all_info['items']:
        updated_time = info['created_at']

        if info['stargazers_count']>200:
            pass








get_rep()




