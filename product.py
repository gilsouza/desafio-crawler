

class Product():
    """
    Classe Produto

    Representação da entidade produto
    """

    def __init__(self, name, title, url):
        """
        Construtor da Classe

        Inicialização da classe

        Arguments:
            name {[string]} -- Nome do produto
            title {[string]} -- Título da página de produto
            url {[string]} -- Url do produto
        """
        self.name = name
        self.title = title
        self.url = url
