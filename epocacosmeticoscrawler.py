import csv
import re

from crawlerbase import CrawlerBase
from product import Product


class EpocacosmeticosCrawler(CrawlerBase):

    def __init__(self, url):
        CrawlerBase.__init__(self, url)

        self.products_visited = set()
        self.file = open('produtos.csv', 'w+')
        self.csv_writer = csv.writer(self.file)

        self.base_url = url

    def dispose(self):

        self.file.close()

    def page_scrap(self, soup):

        product = self.find_product_details(soup)

        self.lock.acquire()

        if product is not None and product.url not in self.products_visited:
            self.products_visited.add(product.url)

            self.csv_writer.writerow(
                [product.name, product.title, product.url])
            self.file.flush()

        self.lock.release()

    def find_product_details(self, soup):

        page_type = soup.find('meta', property='og:type')

        if page_type is not None and page_type.get("content") == "og:product":
            product_name = re.search(
                "productName\":\"([^\"]+)", soup.get_text())
            product_title = re.search(
                "pageTitle\":\"([^\"]+)", soup.get_text())
            product_url = re.search("pageUrl\":\"([^\"]+)", soup.get_text())

            if product_name and product_title and product_url:
                return Product(product_name.group(1), product_title.group(1), product_url.group(1))
