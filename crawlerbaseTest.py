import unittest

from crawlerbase import CrawlerBase
from bs4 import BeautifulSoup


class CrawlerBaseTest(unittest.TestCase):

    def setUp(self):
        self.crawler = CrawlerBase("www.gilsouza.com.br")

    def test_not_raise_exception_scrap(self):
        try:
            url = "lalala"
            self.crawler.scrap(url)
        except:
            self.fail("self.crawler.scrap(url) raised Exception unexpectedly!")

    def test_raise_exception_page_scrap(self):
        soup = BeautifulSoup("<html>data</html>", "html.parser")
        self.assertRaises(NotImplementedError, self.crawler.page_scrap, soup)

    def test_raise_exception_dispose(self):
        self.assertRaises(NotImplementedError, self.crawler.dispose)

if __name__ == '__main__':
    unittest.main()
