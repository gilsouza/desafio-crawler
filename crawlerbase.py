import threading
import requests

from bs4 import BeautifulSoup
from multiprocessing import JoinableQueue


class CrawlerBase:

    def __init__(self, url):
        self.url_to_process = JoinableQueue()
        self.lock = threading.Lock()
        self.url_visited = set()
        self.base_url = url

    def start(self, n_threads):
        self.url_to_process.put(self.base_url)

        for n in range(n_threads):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()

        self.url_to_process.join()

    def worker(self):
        while True:
            try:
                url = self.url_to_process.get(True, timeout=5)
            except queue.Empty:
                break

            if url is not None and url not in self.url_visited:
                self.url_visited.add(url)
                self.scrap(url)

            self.url_to_process.task_done()

    def scrap(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        self.page_scrap(url)

        for link in soup.find_all("a", href=True):
            href = link.get("href")

            if href not in self.url_visited and self.base_url in href:
                self.url_to_process.put(href)

    def page_scrap(self, url):
        print(url)