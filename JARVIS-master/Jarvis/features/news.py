import requests
import json



def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
    news = requests.get(url, timeout=10).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except (KeyError, ValueError, requests.RequestException):
        return False


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
