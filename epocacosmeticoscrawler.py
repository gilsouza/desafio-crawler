import csv
import re

from crawlerbase import CrawlerBase
from product import Product


class EpocacosmeticosCrawler(CrawlerBase):
    """
    Classe com implementação do scrap para a
    página epocacosmeticos.com.br .

    Contém todas as regras necessárias para a extração da informação
    do site conforme desejado.

    Extends:
        CrawlerBase
    """

    def __init__(self, url, file_name = "produtos.csv"):
        CrawlerBase.__init__(self, url)

        try:
            self.products_visited = set()
            self.file = open(file_name, "w+")
            self.csv_writer = csv.writer(self.file)
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo informado não encontrado, favor verificar.")

        self.base_url = url

    def page_scrap(self, soup):
        """
        Sobrescrita do método heradado para regra do crawler.

        Método com as regrás e lógicas necessárias para extrair
        os produtos da página.
        Produtos são escritos no arquivo csv apenas se não foram visitados
        anteriormente.

        Arguments:
            soup {[object]} -- Objeto BeautifulSoup para extração dos produtos
        """
        product = self.find_product_details(soup)

        self.lock.acquire()

        if product is not None and product.url not in self.products_visited:
            self.products_visited.add(product.url)

            self.csv_writer.writerow(
                [product.name, product.title, product.url])
            self.file.flush()

        self.lock.release()

    def find_product_details(self, soup):
        """
        Busca produto na página.

        Busca produto na página se a página for do tipo produto
        e se as informações existirem.

        Arguments:
            soup {[object]} -- Objeto BeautifulSoup para extração dos produtos

        Returns:
            [Product] -- Objeto produto preenchido com nome, título e url
        """
        page_type = soup.find("meta", property="og:type")

        if page_type is not None and page_type.get("content") == "og:product":
            product_name = re.search(
                "productName\":\"([^\"]+)", soup.get_text())
            product_title = re.search(
                "pageTitle\":\"([^\"]+)", soup.get_text())
            product_url = re.search("pageUrl\":\"([^\"]+)", soup.get_text())

            if product_name and product_title and product_url:
                return Product(product_name.group(1), product_title.group(1), product_url.group(1))

    def dispose(self):
        """
        Implementação do método herdado.

        Realiza a limpeza dos objetos, neste caso apenas fecha o arquivo.
        """
        self.file.close()
