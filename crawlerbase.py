import threading
import requests

from bs4 import BeautifulSoup
from multiprocessing import JoinableQueue


class CrawlerBase:
    """
    
    Classe base para realizar scrap de urls.
    
    Classe que contem a fila das urls que serão processadas
    e realizará o controle do que já foi acessado.
    A classe deve ser estendida para que haja a implementação
    de acordo com a necessidade da página.
    """
    def __init__(self, url):
        """
        Construtor Base do Crawler

        Inicializa váriaveis de instância para controle e constantes.

        Arguments:
            url {[string]} -- url base para inicio e definição de contexto
                para que o crawler possa se restringir a url.
        """
        self.TIMEOUT_QUEUE = 5
        self.url_to_process = JoinableQueue()
        self.lock = threading.Lock()
        self.url_visited = set()
        self.base_url = url

    def start(self, n_threads):
        """
        Início da execução do crawler.
        
        É onde se recebe a url inicial e a partir delas é realizada a
        busca por outras.
        
        Arguments:
            n_threads {[int]} -- Número de threads utilizadas
        """
        self.url_to_process.put(self.base_url)

        for n in range(n_threads):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()

        self.url_to_process.join()
        self.dispose()

    def worker(self):
        """
        Worker (método) utilizado como target pelas threads.

        Método responsável por processar a fila de urls até que 
        a mesma esteja vazia através de um loop infinito com
        condição de saída.
        """
        while True:
            try:
                url = self.url_to_process.get(True, timeout=self.TIMEOUT_QUEUE)
            except queue.Empty:
                break

            if url is not None and url not in self.url_visited:
                self.url_visited.add(url)
                self.scrap(url)

            self.url_to_process.task_done()

    def scrap(self, url):
        """
        Busca por mais urls na página e realiza scrap conforme implementação

        Método responsável por iniciar o scrap da url para retroalimentar
        a fila de urls com os links encontrados na página.

        Arguments:
            url {[string]} -- url onde o scrap será realizado
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
        except:
            return

        self.page_scrap(soup)

        for link in soup.find_all("a", href=True):
            href = link.get("href")

            if href not in self.url_visited and self.base_url in href:
                self.url_to_process.put(href)

    def page_scrap(self, soup):
        """
        Método abstrato para scrap da página de acordo com regras.
        
        Este método é responsável por conter toda a lógica necessária
        para realizar o scrap da página.
        
        Arguments:
            soup {[object]} -- Objeto BeautifulSoup para manipulação do scrap
        
        Raises:
            NotImplementedError -- Quando não implementado
        """
        raise NotImplementedError()

    def dispose(self):
        """
        Método para limpeza de objetos.
        
        Ao final da execução do crawler este método é chamado para realizar
        a limpeza dos objetos.
        
        Raises:
            NotImplementedError -- Quando não implementado
        """
        raise NotImplementedError()        