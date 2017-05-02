from epocacosmeticoscrawler import EpocacosmeticosCrawler


if __name__ == "__main__":
    c = EpocacosmeticosCrawler("http://www.epocacosmeticos.com.br")
    c.start(20)