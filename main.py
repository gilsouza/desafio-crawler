from crawlerbase import CrawlerBase


if __name__ == "__main__":
    c = CrawlerBase("http://www.epocacosmeticos.com.br")
    c.start(20)