import requests
import datetime as dt

HOST = 'https://api.stackexchange.com'
uri = '/2.3/questions?'


def stack_question(tag, days):
    url = HOST + uri
    todate = int(dt.datetime.fromisoformat(str(dt.datetime.today())).timestamp())
    fromdate = int(dt.datetime.fromisoformat(str(dt.date.today() - dt.timedelta(days=days))).timestamp())

    for page in range(1, 25):
        params = {
            'fromdate': fromdate,
            'todate': todate,
            'order': 'desc',
            'sort': 'activity',
            'tagged': tag,
            'site': 'stackoverflow',
            'page': page,
            'pagesize': 100
        }
        request = requests.get(url, params=params).json()
        for question in request['items']:
            print(dt.datetime.utcfromtimestamp(question['creation_date']), question['title'], question['link'])


stack_question('Python', 2)
