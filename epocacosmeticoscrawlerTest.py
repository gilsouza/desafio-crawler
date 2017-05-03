import unittest

from epocacosmeticoscrawler import EpocacosmeticosCrawler
from bs4 import BeautifulSoup
from product import Product


class EpocacosmeticosCrawlerTest(unittest.TestCase):

    def setUp(self):
        """ URL mal formatada para utilização dos testes. """
        self.fake_url = "www.gilsouza.com.br"

    def test_raise_filenotfound_exception(self):
        """ Teste de inicialização da classe com arquivo inexistente """
        self.assertRaises(FileNotFoundError, EpocacosmeticosCrawler,
                          self.fake_url, "teste/product.csv")

    def test_scrap_product_page(self):
        """ Teste do método page_scrap para uma página de produto """
        file = open("resource_test/productpage.txt", "r")

        soup = BeautifulSoup(file.read(), "html.parser")

        crawler = EpocacosmeticosCrawler(self.fake_url, "EpocacosmeticosCrawlerTest.csv")
        crawler.page_scrap(soup)
        crawler.dispose()

        file.close()

        file = open("EpocacosmeticosCrawlerTest.csv", "r")

        self.assertEqual(file.read().strip(), "Nuit Rose Limited Edition Fiorucci - Perfume Feminino - Deo Colônia - 100ml,"
            + "Perfume Nuit Rose Limited Edition Fiorucci Feminino - Época Cosméticos,"
            + "http://www.epocacosmeticos.com.br/nuit-rose-limited-edition-deo-colonia-fiorucci-perfume-feminino/p")
        
        file.close()

    def test_scrap_not_product_page(self):
        """ Teste do método page_scrap para uma página de "categoria" """
        file = open("resource_test/categorypage.txt", "r")

        soup = BeautifulSoup(file.read(), "html.parser")

        crawler = EpocacosmeticosCrawler(self.fake_url, "EpocacosmeticosCrawlerTest.csv")
        crawler.page_scrap(soup)
        crawler.dispose()

        file.close()

        file = open("EpocacosmeticosCrawlerTest.csv", "r")

        self.assertEqual(file.read().strip(), "")
        
        file.close()

    def test_product_details_product_page(self):
        """ Teste do scrap de produto em uma página de produto """
        file = open("resource_test/productpage.txt", "r")

        soup = BeautifulSoup(file.read(), "html.parser")

        crawler = EpocacosmeticosCrawler(self.fake_url, "EpocacosmeticosCrawlerTest.csv")
        product = crawler.find_product_details(soup)
        crawler.dispose()

        file.close()

        self.assertTrue(isinstance(product,Product))

    def test_product_details_not_product_page(self):
        """ Teste do scrap de produto em uma página de categoria """
        file = open("resource_test/categorypage.txt", "r")

        soup = BeautifulSoup(file.read(), "html.parser")

        crawler = EpocacosmeticosCrawler(self.fake_url, "EpocacosmeticosCrawlerTest.csv")
        product = crawler.find_product_details(soup)
        crawler.dispose()

        file.close()

        self.assertFalse(isinstance(product,Product)) 



if __name__ == '__main__':
    unittest.main()
