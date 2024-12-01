import requests
from bs4 import BeautifulSoup

class Crawler:
    keyword = None

    def __init__(self, keyword):
        self.keyword = keyword

    def test(self):
        print(self.keyword)

crawlerInstances = Crawler("")
crawlerInstances.test()