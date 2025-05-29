
import requests
from bs4 import BeautifulSoup

def get_sec_filing(url="https://www.sec.gov/edgar/search"):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.title.string
