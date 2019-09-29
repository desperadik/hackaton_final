from urllib.parse import urlparse


def run():
    
    url = 'http://opendata.trudvsem.ru/7710538364-professions/professions.xml#135388'
    print(urlparse(url))


run()