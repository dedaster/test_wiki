import pytest
import requests
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
headers = {'user-agent': 'Mozilla/5.0'}

@pytest.fixture(scope="function")
def browser():
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
