import requests
from bs4 import BeautifulSoup as Soup

s = requests.session()
r = s.get('http://www.urbandead.com/map.cgi?username=MaltonMapper1&password=urbandead')

soup = Soup(r.text, 'html.parser')


def getPage(soup):
    r = s.get('http://www.urbandead.com/map.cgi?username=MaltonMapper1&password=urbandead')
    soup = Soup(r.text, 'html.parser')
    return soup




class Walker:
    pos = [0,0]
    loc = ""
    cade = ""

    b = {"doors secured":0, 'loosely barricaded':1, 'lightly barricaded':2, 'quite strongly barricaded':3,
         'very strongly barricaded':4, 'heavily barricaded':5, 'very heavily barricaded':6,
         'extremely heavily barricaded':7, 'wide open': -1}