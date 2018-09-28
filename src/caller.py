import requests

def get_text_from_url(url):
    return requests.get(url).text