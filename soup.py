from bs4 import BeautifulSoup
import requests

result = requests.get('https://news.google.com/covid19/map?hl=en-CA&mid=/m/0d060g&gl=CA&ceid=CA:en').text
soup = BeautifulSoup(result, 'html.parser')


def confirmed():
    confirmed = soup.find_all('div', {'class': 'UvMayb'})[0].text
    return confirmed


def recovered():
    recovered = soup.find_all('div', {'class': 'UvMayb'})[1].text
    return recovered


def fatalities():
    fatalities = soup.find_all('div', {'class': 'UvMayb'})[2].text
    return fatalities

