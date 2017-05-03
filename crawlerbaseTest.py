import unittest

from bs4 import BeautifulSoup
from crawlerbase import CrawlerBase
from product import Product

import csv
import re


class ExtendedTestCrawler(CrawlerBase):
    """Extenção de CrawlerBase

    Classe com implementação dos métodos page_scrap e dispose

    Extends:
        CrawlerBase

    """

    def __init__(self, url, file_name="CrawlerBaseTest.csv"):
        CrawlerBase.__init__(self, url)

        try:
            self.products_visited = set()
            self.file = open(file_name, "w+")
            self.csv_writer = csv.writer(self.file)
        except FileNotFoundError:
            raise FileNotFoundError(
                "Arquivo informado não encontrado, favor verificar.")

        self.base_url = url

    def page_scrap(self, soup):
        """Implementação de page_scrap

        Implementação realizada para testes

        Arguments:
            soup {[type]} -- Objeto BeautifulSoup
        """
        self.lock.acquire()
        self.csv_writer.writerow("scrap!")
        self.file.flush()
        self.lock.release()

    def dispose(self):
        """
        Implementação do método herdado.

        Realiza a limpeza dos objetos, neste caso apenas fecha o arquivo.
        """
        self.file.close()


class CrawlerBaseTest(unittest.TestCase):

    def setUp(self):
        """ URL mal formatada para utilização dos testes. """
        self.crawler_url_error = CrawlerBase("www.epocacosmeticos.com.br")

    def test_not_raise_exception_scrap(self):
        """ Testa se o crawler levanta exceção quando usada uma 
            url mal formatada. """
        try:
            url = "lalala"
            self.crawler_url_error.scrap(url)
        except:
            self.fail(
                "self.crawler_url_error.scrap(url) raised Exception unexpectedly!")

    def test_raise_exception_page_scrap(self):
        """ Testa exceção para método não implementado. """
        soup = BeautifulSoup("<html>data</html>", "html.parser")
        self.assertRaises(NotImplementedError,
                          self.crawler_url_error.page_scrap, soup)

    def test_raise_exception_dispose(self):
        """ Testa exceção para método não implementado. """
        self.assertRaises(NotImplementedError, self.crawler_url_error.dispose)

    def test_crawler_extends(self):
        """ Testa implementação do Crawler através da herança da classe base. """
        crawler = ExtendedTestCrawler("http://www.gilsouza.com.br")
        crawler.start(1)

        file = open("CrawlerBaseTest.csv")
        self.assertEqual(file.read().strip(), "s,c,r,a,p,!")
        file.close()

if __name__ == '__main__':
    unittest.main()
